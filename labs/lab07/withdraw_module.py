import mysql.connector
import hashlib


def verify_pin(card_no, pin):
    try:
        conn = mysql.connector.connect(
            user="root",
            password="123456",
            database="atm_demo"
        )
        cur = conn.cursor()
        cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
        row = cur.fetchone()
        conn.close()

        if row and row[0] == hashlib.sha256(pin.encode()).hexdigest():
            return True
        else:
            return False
    except mysql.connector.Error as e:
        print("Database connection error:", e)
        return False


def withdraw(card_no, amount):
    try:
        conn = mysql.connector.connect(
            user="root",
            password="123456",
            database="atm_demo"
        )
        cur = conn.cursor()

        conn.start_transaction()
        cur.execute("""
            SELECT account_id, balance 
            FROM accounts 
            JOIN cards USING(account_id) 
            WHERE card_no=%s 
            FOR UPDATE
        """, (card_no,))

        result = cur.fetchone()
        if not result:
            raise Exception("Card not found")

        account_id, balance = result
        balance = float(balance)  

        if balance < amount:
            raise Exception("Insufficient funds")

        new_balance = balance - amount

    
        cur.execute("UPDATE accounts SET balance=%s WHERE account_id=%s", (new_balance, account_id))

        cur.execute("""
            INSERT INTO transactions(account_id, card_no, atm_id, tx_type, amount, balance_after)
            VALUES (%s, %s, 1, 'WITHDRAW', %s, %s)
        """, (account_id, card_no, amount, new_balance))

        conn.commit()
        print(f"✅ Withdraw success! Amount: {amount:.2f}, New balance: {new_balance:.2f}")

    except Exception as e:
        conn.rollback()
        print("⚠️ Error:", e)

    finally:
        conn.close()


# --- Chạy thử chương trình ---
if __name__ == "__main__":
    print("=== ATM Withdraw System ===")
    card_no = input("Enter card number: ")
    pin = input("Enter PIN: ")

    if verify_pin(card_no, pin):
        try:
            amount = float(input("Enter amount to withdraw: "))
            withdraw(card_no, amount)
        except ValueError:
            print("⚠️ Invalid amount format.")
    else:
        print("❌ Invalid card or PIN.")
