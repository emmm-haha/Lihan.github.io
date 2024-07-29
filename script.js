// script.js

// 显示或隐藏返回顶部按钮
window.onscroll = function() {
    const button = document.getElementById("back-to-top");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
};

// 滚动回到顶部
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}