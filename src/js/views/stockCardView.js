import * as img from '../../../src/img/logo/*'

class stockCardView {
    #main = document.querySelector(".main");
    #i;
    #data;
    #value;
    #my_money;
    account;
    data_to_holding = {};
    data_to_transaction = {};
    #quantity;
    buy_button;
    #dis = 1

    render(data, company_title, account, saveHoldingTransaction, changeAccount){
        this.#data = data;
        this.account = account
        const markup = this.#generateMarkup();
        this.#clearMain();
        this.#main.insertAdjacentHTML('afterbegin', markup);
        this.#dataRender(company_title);
        this.#addQuantity(company_title);
        this.#buyStocks(company_title, saveHoldingTransaction, changeAccount);
        this.buy_button = document.getElementById("buy")
    }

    #clearMain() {
        this.#main.innerHTML = '';
    }

    #addQuantity(company) {
        const counter = document.getElementById('num_count');
        const plus = document.getElementById('plus');
        const minus = document.getElementById('minus');

        
        let self = this
        for (let i = 0; i < this.#data.length; ++i) {
            if(company === this.#data[i].title){
                let purchase_bottom = document.getElementsByClassName("purchase_bottom_price")[0]
                let price_left = document.getElementsByClassName("price_left")[0]
                price_left.innerHTML = `
                    <p>Цена за акцию: ${this.#data[i].price_per_share} $</p>
                `

                plus.onclick = function() {
                    self.#dis = self.#dis + 1;
                    counter.setAttribute("value", self.#dis) 
                    self.#quantity = self.#dis
                    let cost_plus = self.#data[i].price_per_share * self.#dis
                    
                    self.#value = self.#data[i].price_per_share * self.#dis

                    purchase_bottom.innerHTML = `
                    <p>Стоимость: ${cost_plus.toFixed(2)} $</p>
                    `
                    

                }
        
                minus.onclick = function() {
                    if(dis > 0) {
                        dis = dis - 1;
                        counter.setAttribute("value", self.#dis) 
                    }        
                    let cost_minus = self.#data[i].price_per_share * self.#dis
                    self.#value = self.#data[i].price_per_share * self.#dis

                    purchase_bottom.innerHTML = `
                        <p>Стоимость: ${cost_minus.toFixed(2)} $</p>
                    `
                    
                }
            }
        }

        
    }


    #generateMarkup() {
        return `
            <div class="cardMain">
                <div class="companyInfo">
                    <div class="aboutcompany">
                        <div class="imageses">
                            
                        </div>
                        <div class="imageinfo">


                        </div>
                        <div class="textex">
                            <div class="price_left"></div>
                            <p class="lef">Ожидаемая цена: 23.4 $</p>
                            <p class="lef">Доходность за 6 мес: 4.5 %</p>
                            <p class="lef">Дивидендный доход: 1.03 $</p>
                        </div>
                    </div>
                    <div class="aboutCompanyInformation">

                    </div>
                </div>

                <div class="apurchase">
                    <div class="purchase">
                        <div class="ptop">
                

                        </div>
                        <div class="quantity_goods">
                            <input type="button" value="-" id="minus" class="adjuster">
                            <input type="number" step="1" min="1" max="10" id="num_count" name="quantity" value="1" title="Qty" class="quantity">
                            <input type="button" value="+" id="plus" class="adjuster">
                        </div>
                        <hr>
                        <div class="purchase_bottom">
                            <div class="my_acc"><p>Ваш счет: ${Number(this.account.account).toFixed(2)} $</p></div>
                            <p>Коммисиия Банка:</p>
                            <p>Брокерская комиссия:</p>
                            <div class="purchase_bottom_price"><p>Стоимость: 44.22 $</p></div>
                            <div class="purchase_btn">
                                <button>Добавить в корзину</button>
                                <button id="buy">Купить</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `
    } 

    #buyStocks(company, saveHoldingTransaction, changeAccount){
        for (let i = 0; i < this.#data.length; ++i) {
            if(company === this.#data[i].title){
                let purchase_bottom = document.getElementsByClassName("purchase_bottom_price")[0]
                let buy = document.getElementById("buy")
                this.#quantity = this.#dis
                this.#value = this.#data[i].price_per_share * this.#dis

                purchase_bottom.innerHTML = `
                <p>Стоимость: ${this.#value.toFixed(2)} $</p>
                `
                let my_mony = document.getElementsByClassName("my_acc")[0]



                let self = this 
                buy.addEventListener("click", function(){
                    self.#my_money = self.account.account - self.#value

                    
                    my_mony.innerHTML = `
                    <p>Ваш счет: ${self.#my_money.toFixed(2)} $</p>
                    ` 

                    self.account.account = self.#my_money.toFixed(2)

                    self.data_to_holding = {
                          title: self.#data[i].title,
                          symbol: self.#data[i].symbol,
                          price_per_share: self.#data[i].price_per_share,
                          total_price: self.#value.toFixed(2),
                          quantity: self.#quantity
                        }
                    
                    self.data_to_transaction = {
                        title: self.#data[i].title,
                        symbol: self.#data[i].symbol,
                        price_per_share: self.#data[i].price_per_share,
                        action: 'bought',
                        total_price: self.#value.toFixed(2),
                        quantity: self.#quantity
                    }

                    saveHoldingTransaction(self.data_to_holding, self.data_to_transaction) 
                    changeAccount(self.account)

                })
            }
        }
    }


    #dataRender(company) {
        for (let i = 0; i < this.#data.length; ++i) {
            if(company === this.#data[i].title){
                
                let stock_upper = document.getElementsByClassName("ptop")[0]
                
                stock_upper.innerHTML =  `   
                    <p class="pabc">${this.#data[i].title}</p>
                    <p class="ptitle">${this.#data[i].symbol}</p>
                `   

                let description = document.getElementsByClassName("aboutCompanyInformation")[0]

                description.innerHTML = `
                    <ul>
                        <h2>О компании ${this.#data[i].title}</h2>
                        <p>${this.#data[i].description}</p>
                    </ul>
                `

                let main_title = document.getElementsByClassName("imageinfo")[0]

                main_title.innerHTML = `
                    <p class="stitle">${this.#data[i].title}</p>
                    <p class="sabc">${this.#data[i].symbol}</p>
                `
                
                let image = document.getElementsByClassName("imageses")[0]
                
                image.innerHTML = `
                    <img src="${img[this.#data[i].title + ".png"]}" alt="${this.#data[i].title}" class="label">
                `        
            }
        }
    }

}

export default new stockCardView();

