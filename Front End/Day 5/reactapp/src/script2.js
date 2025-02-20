document.addEventListener('mousemove', function(event) {
    const pop = document.createElement('div');
    pop.classList.add('pop');
    pop.style.left = `${event.pageX - 50}px`;
    pop.style.top = `${event.pageY - 50}px`;
    document.body.appendChild(pop);
    pop.style.transform = 'translateY(-30px)';
    setTimeout(() => {
        pop.remove();
    }, 1000);
});
