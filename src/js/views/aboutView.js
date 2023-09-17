import * as img from '../../../src/img/*'

class aboutView {
    #main = document.querySelector(".main");


    render(user){
        const markup = this.#generateMarkup();
        this.#clearMain();
        this.#main.insertAdjacentHTML('afterbegin', markup);
        this.#slider();
        this.#restrictAccess(user)
    }

    #clearMain() {
        this.#main.innerHTML = '';
    }

    #generateMarkup() {
        return `
            <div class="honetitle"> 
            
                <h1>Фондовый рынок</h1>

            </div>

            <br>
            <!-- Slideshow container -->
            <div class="slideshow-container">

                <!-- Full-width images with number and caption text -->
                <div class="mySlides fade">
                    <img src="${img['1.jpg']}" width="1000" height="500">
                </div>
            
                <div class="mySlides fade">
                    <img src="${img['2.jpg']}" width="1000" height="500">
                </div>
            
                <div class="mySlides fade">
                    <img src="${img['3.jpg']}" width="1000" height="500">
                </div>
            
                <div class="mySlides fade">
                    <img src="${img['4.jpg']}" width="1000" height="500">
                </div>

                <!-- Next and previous buttons -->
                <a class="prev">&#10094;</a>
                <a class="next">&#10095;</a>
            </div>

            <br>
            
            <!-- The dots/circles -->
            <div style="text-align:center">
                <span class="dot"></span>
                <span class="dot"></span>
                <span class="dot"></span>
                <span class="dot"></span>
            </div>
            
            <div>
                <p class="shorts">Знание - это успех Когда дело касается ваших денег, знания - бесценны.</p>
            </div>

            <hr width="70%">

            <div class="ram">
                <p class="long">
                    Владение ценными бумагами и прочими финансовыми инструментами всегда сопряжено с рисками: 
                    стоимость ценных бумаг и прочих финансовых инструментов может расти или падать. Результаты инвестирования в 
                    прошлом не гарантируют доходов в будущем. В соответствии с законодательством, компания не гарантирует и не 
                    обещает в будущем доходности вложений, не дает гарантии надежности возможных инвестиций и стабильности размеров возможных доходов.
                </p>
            </div>
    `
    }     

    #slider() {
        
        let slideIndex = 1;
        showSlides(slideIndex);
        
            // Next/previous controls
        function plusSlides(n) {
            showSlides(slideIndex += n);
        }        
        function currentSlide(i) {
            showSlides(slideIndex = i);
        }       

        for(let i=0; i < 4; i++){
            
            document.querySelectorAll(".dot")[i].addEventListener("click", function() {currentSlide(i)})
        }

        document.querySelector(".prev").addEventListener("click", function() {plusSlides(-1)})
        document.querySelector(".next").addEventListener("click", function() {plusSlides(1)})

        function showSlides(n) {
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            if (n > slides.length) {slideIndex = 1}
            if (n < 1) {slideIndex = slides.length}
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active", "");
            }
            slides[slideIndex-1].style.display = "block";
            dots[slideIndex-1].className += " active";
        }
    }

    #restrictAccess(user) {
        if(user == undefined) {
            document.querySelector(".support").style.display = "none"
        } else {
            document.querySelector(".support").style.display = "flex"
        }
    }

}

export default new aboutView();



