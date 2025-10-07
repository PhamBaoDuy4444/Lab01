// ===== Utilities =====
const $ = (sel) => document.querySelector(sel);
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/i;

function showError(el, msg){
  el.textContent = msg || "";
}
function clearMessages(){
  showError($("#usernameError"), "");
  showError($("#passwordError"), "");
  const fm = $("#formMessage");
  fm.textContent = "";
  fm.className = "form-message";
}

function setBusy(state){
  const btn = $("#loginBtn");
  btn.disabled = state;
  btn.textContent = state ? "Processing..." : "Login";
}

function saveRemembered(){
  const remember = $("#remember").checked;
  const username = $("#username").value.trim();
  if(remember && username){
    localStorage.setItem("remember_username", username);
    localStorage.setItem("remember_flag", "1");
  } else {
    localStorage.removeItem("remember_username");
    localStorage.removeItem("remember_flag");
  }
}

function loadRemembered(){
  const flag = localStorage.getItem("remember_flag");
  const val = localStorage.getItem("remember_username") || "";
  if(flag === "1" && val){
    $("#username").value = val;
    $("#remember").checked = true;
  }
}

// ===== Validation =====
function validateUsername(value){
  if(!value) return "Vui lòng nhập Username.";
  if(value.length < 3) return "Username tối thiểu 3 ký tự.";
  if(value.includes("@") && !emailRegex.test(value)){
    return "Email không hợp lệ.";
  }
  return "";
}

function validatePassword(value){
  if(!value) return "Vui lòng nhập Password.";
  if(value.length < 6) return "Password tối thiểu 6 ký tự.";
  // kiểm tra độ mạnh cơ bản (khuyến nghị, không bắt buộc)
  const hasLetter = /[A-Za-z]/.test(value);
  const hasNumber = /\d/.test(value);
  if(!(hasLetter && hasNumber)){
    return "Nên gồm cả chữ và số để an toàn hơn.";
  }
  return "";
}

// ===== Main =====
document.addEventListener("DOMContentLoaded", () => {
  loadRemembered();

  // toggle show/hide password
  $(".toggle").addEventListener("click", () => {
    const p = $("#password");
    p.type = p.type === "password" ? "text" : "password";
  });

  $("#cancelBtn").addEventListener("click", () => {
    $("#loginForm").reset();
    clearMessages();
    saveRemembered(); // sẽ xoá nếu không tick
  });

  $("#forgot").addEventListener("click", (e) => {
    e.preventDefault();
    const fm = $("#formMessage");
    fm.textContent = "Demo: Tính năng quên mật khẩu chưa kết nối email.";
    fm.className = "form-message";
  });

  $("#loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    clearMessages();

    const username = $("#username").value.trim();
    const password = $("#password").value;

    const uErr = validateUsername(username);
    const pErr = validatePassword(password);

    showError($("#usernameError"), uErr);
    showError($("#passwordError"), pErr);

    if(uErr || pErr){
      $("#formMessage").textContent = "Vui lòng sửa lỗi và thử lại.";
      $("#formMessage").className = "form-message error";
      return;
    }

    try{
      setBusy(true);
      // giả lập gọi API
      await new Promise(r => setTimeout(r, 800));

      saveRemembered();

      $("#formMessage").textContent = "Đăng nhập thành công (demo).";
      $("#formMessage").className = "form-message success";

      // reset field password cho an toàn
      $("#password").value = "";
    } catch(err){
      $("#formMessage").textContent = "Có lỗi xảy ra. Vui lòng thử lại.";
      $("#formMessage").className = "form-message error";
    } finally{
      setBusy(false);
    }
  });
});
