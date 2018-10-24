(function() { 
    
    var score = 0;
    var xchange = 0;
    var ychange = 0;
    var canvas;
    var context;
    var width;
    var height;
    var interval_id;
    var moveUp = false;
    var moveDown = false;
    var moveLeft = false;
    var moveRight = false;
    var snake = {
        x : 50,
        y : 150,
        size : 10
    };
    var food;
    
    document.addEventListener('DOMContentLoaded', init, false);
    
    function init() {
        canvas = document.querySelector('canvas');
        context = canvas.getContext('2d');
        width = canvas.width;
        height = canvas.height;
        window.addEventListener('keydown', pressed, false);
        window.addEventListener('keyup', unpressed, false);
        interval_id = window.setInterval(draw, 33);
        food = {
        x : getRandomNumber(0, canvas.width),
        y : getRandomNumber(0, canvas.height),
        size : 10,
        color : 'limegreen'
        };
    }
    
    function draw() {
        context.clearRect(0, 0, width, height)
        context.fillStyle = 'black';
        context.fillRect(snake.x, snake.y, snake.size, snake.size);
        if(snake.y < 0 || snake.y + snake.size >= height ||
            snake.x + snake.size >= width || snake.x < 0) {
            stop();
            window.alert('you lose' + ' your score is: ' + score)
            return
        }
        if (collides(food)) {
            score += 1;
            food.x = getRandomNumber(0, canvas.width)
            food.y = getRandomNumber(0, canvas.height)
        }
        else {
            context.fillStyle = food.color;
            context.fillRect(food.x, food.y, food.size, food.size);
        }
        if (moveUp) {
            ychange = -3;
            xchange = 0;
        }
        if (moveDown) {
            ychange = 3;
            xchange = 0;
        }
        if(moveLeft) {
            ychange = 0;
            xchange = -3;
        }
        if(moveRight) {
            ychange = 0;
            xchange = 3;
        }
        snake.x += xchange
        snake.y += ychange
    }
    
    function collides(food) {
        if (snake.x + snake.size < food.x ||
            food.x + food.size < snake.x ||
            snake.y > food.y + food.size ||
            food.y > snake.y + snake.size) {
            return false;
        } 
        else {
            return true;
        }
    }
    
    function stop() {
        clearInterval(interval_id);
        window.removeEventListener('keyDown', pressed);
        window.removeEventListener('keyUp', unpressed);
    }
    
    function pressed(event) {
        var keyCode = event.keyCode;
        if (keyCode === 38) {
            moveUp = true;
        }
        else if (keyCode === 40) {
            moveDown = true;
        }
        else if (keyCode === 37) {
            moveLeft = true;
        }
        else if (keyCode === 39) {
            moveRight = true;
        }
    }
    
    function unpressed(event) {
        var keyCode = event.keyCode;
        if (keyCode === 38) {
            moveUp = false;
        }
        else if (keyCode === 40) {
            moveDown = false;
        }
        else if (keyCode === 37) {
            moveLeft = false;
        }
        else if (keyCode === 39) {
            moveRight = false;
        }
    }
    
    function getRandomNumber(min, max) {
        return Math.round(Math.random() * (max - min)) + min;
    }
    
})(); 