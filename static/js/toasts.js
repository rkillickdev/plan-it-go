const toast = document.querySelector('#my-toast');

document.addEventListener("DOMContentLoaded", () => {
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance
  (toast);
  toastBootstrap.show();
});
