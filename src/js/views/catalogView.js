import * as img from '../../../src/img/logo/*'
import stockCardView from './stockCardView';


class catalogView {
    #main = document.querySelector(".main");
    #acc = document.getElementsByClassName("flip");
    #i;
    #data;



    render(data){
        this.#data = data;
        const markup = this.#generateMarkup();
        this.#clearMain();
        this.#main.insertAdjacentHTML('afterbegin', markup);
        this.#dataRender();
    }

    #clearMain() {
        this.#main.innerHTML = '';
    }

    #generateMarkup() {
        return `
        <div class="catalogPage">
            <div class="all">
                <div class="catalog">
                    <div class="card">
                        <div><img src="${img['3M.png']}" alt="3M"></div>
                        <div class="stock">
                            
                            
                        </div>
                        <button class="catalogBtn" value="3M" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['Amazon.com.png']}" alt="Amazon.com"></div>
                        <div class="stock">

                            
                        </div>
                        <button class="catalogBtn" value="Amazon.com" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['Campbell Soup.png']}" alt="Campbell Soup"></div>
                        <div class="stock">

                            
                        </div>
                        <button class="catalogBtn" value="Campbell Soup" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['Disney.png']}" alt="Disney"></div>
                        <div class="stock">

                            
                        </div>
                        <button class="catalogBtn" value="Disney" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['Dow Chemical.png']}" alt="Dow Chemical"></div>
                        <div class="stock">
 
                            
                        </div>
                        <button class="catalogBtn" value="Dow Chemical" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['Exxon Mobil.png']}" alt="Exxon Mobil"></div>
                        <div class="stock">
                            
                            
                        </div>
                        <button class="catalogBtn" value="Exxon Mobil" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['Ford.png']}" alt="Ford"></div>
                        <div class="stock">
                           
                            
                        </div>
                        <button class="catalogBtn" value="Ford" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['The Gap.png']}" alt="The Gap"></div>
                        <div class="stock">
                          
                           
                        </div>
                        <button class="catalogBtn" value="The Gap" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['General Mills.png']}" alt="General Mills"></div>
                        <div class="stock">
                            
                            
                        </div>
                        <button class="catalogBtn" value="General Mills" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['Hewlett Packard.png']}" alt="Hewlett Packard"></div>
                        <div class="stock">
                            
                            
                        </div>
                        <button class="catalogBtn" value="Hewlett Packard" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['IBM.png']}" alt="IBM"></div>
                        <div class="stock">
                            
                            
                        </div>
                        <button class="catalogBtn" value="IBM" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    <div class="card">
                        <div><img src="${img['Johnson & Johnson.png']}" alt="Johnson & Johnson"></div>
                        <div class="stock">
                           
                           
                        </div>
                        <button class="catalogBtn" value="Johnson & Johnson" onclick="window.showCardCompany(); return false;">Подробнее</button>
                    </div>

                    </div>
                </div>
            </div>
        </div>
    `
    } 


    #dataRender() {
        
        for (let i = 0; i < this.#data.length; ++i) {
            let stock_card = document.getElementsByClassName("stock")[i]
            stock_card.innerHTML =  `   
                <p class="top">${this.#data[i].title}</p>
                <p class="middle">${this.#data[i].symbol}</p>
                <p class="bottom">${this.#data[i].price_per_share}</p>
            `
            
        }
    }

}

export default new catalogView();