window.onload = function () {
    const popup = document.getElementById("welcome-popup");
    const btnClose = document.getElementById("close-popup");

    popup.style.display = "flex";
    
    btnClose.addEventListener("click", () => {
        popup.style.display = "none";
    });
};
