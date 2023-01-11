const slideWidth = window.matchMedia('(max-width: 600px)').matches ? 300 : 500;

window.onload = function () {
    // Show the buttons if JS is enabled
    document.getElementById('slider-buttons').classList.remove('hidden');

    document.getElementById('slider-back').onclick = function(event) {
        event.target.disabled = true;
        let div = document.getElementById('slides');
        let position = div.scrollLeft;
        let newPosition = Math.max(position - slideWidth);
        div.scrollTo({left: newPosition, behavior: 'smooth'});
        window.setTimeout(() => {
            event.target.disabled = false;
        }, 500);
    };

    document.getElementById('slider-forward').onclick = function(event) {
        event.target.disabled = true;
        let div = document.getElementById('slides');
        let position = div.scrollLeft;
        let newPosition = Math.min(position + slideWidth);
        div.scrollTo({left: newPosition, behavior: 'smooth'});
        window.setTimeout(() => {
            event.target.disabled = false;
        }, 500);
    };
};
