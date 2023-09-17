class aboutCompanyView {
    #main = document.querySelector(".main");

    render(){
        const markup = this.#generateMarkup();
        this.#clearMain();
        this.#main.insertAdjacentHTML('afterbegin', markup);
    }


    #clearMain() {
        this.#main.innerHTML = '';
    }

    #generateMarkup() {
        return `
            <div class="page">
                <div class="companyText">
                    <h1>О компании</h1>
                    <span class="textp">
                        <p>
                            Konya Broker - системообразующая инвестиционная компания международного уровня, представленная в 12 странах: Казахстан, США, Германия, Великобритания, Украина, Кыргызстан,
                            Узбекистан, Азербайджан, Кипр, Франция и Испания.
                        </p>
            
                        <hr>

                        <p>
                            Компания входит в международную инвестиционную группу Freedom Holding Corp. Собственный капитал группы превышает $508 000 000.
                        </p>
                    </span>
                </div>
            </div>
        `
    } 
}

export default new aboutCompanyView();






