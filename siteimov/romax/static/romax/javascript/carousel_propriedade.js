let slideIndex = 0;
        const slides = document.querySelectorAll('.carousel-image');

        function showSlides() {
            slides.forEach(slide => {
                slide.style.display = 'none';
            });
            if (slideIndex >= slides.length) {
                slideIndex = 0;
            } else if (slideIndex < 0) {
                slideIndex = slides.length - 1;
            }
            slides[slideIndex].style.display = 'block';
        }

        function prevSlide() {
            slideIndex--;
            showSlides();
        }

        function nextSlide() {
            slideIndex++;
            showSlides();
        }
        showSlides();