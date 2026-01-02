// 1. Mobile Menu Toggle
document.querySelector('.header-toggle').addEventListener('click', function() {
    document.body.classList.toggle('header-show');
    this.classList.toggle('bi-list');
    this.classList.toggle('bi-x');
});

// 2. Initialize AOS
AOS.init({ duration: 800, once: true });

// 3. Custom Pointer Logic
const cursorDot = document.querySelector(".cursor-dot");
const cursorOutline = document.querySelector(".cursor-outline");

if (cursorDot && cursorOutline) {
    window.addEventListener("mousemove", function (e) {
        const posX = e.clientX;
        const posY = e.clientY;

        cursorDot.style.left = `${posX}px`;
        cursorDot.style.top = `${posY}px`;

        cursorOutline.animate({
            left: `${posX}px`,
            top: `${posY}px`
        }, { duration: 500, fill: "forwards" });
    });

    const targets = document.querySelectorAll("a, button, .expertise-card, .case-study-card, input, textarea");
    targets.forEach(link => {
        link.addEventListener("mouseenter", () => document.body.classList.add("cursor-active"));
        link.addEventListener("mouseleave", () => document.body.classList.remove("cursor-active"));
    });
}

// 4. Swiper Initialization
function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
        let config = JSON.parse(
            swiperElement.querySelector(".swiper-config").innerHTML.trim()
        );
        new Swiper(swiperElement, config);
    });
}
window.addEventListener("load", initSwiper);