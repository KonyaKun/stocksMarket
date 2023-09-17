class holdingsView {
    #main = document.querySelector(".main");
    #paginated_data;
    account;
    data_to_transaction;
    data_to_holdings;
    sell_button;
    next_page;
    previous_page;
    pages;


    render(paginated_data, pagination, func, 
        saveHoldingsToTransaction, 
        saveHoldingsToHoldings, account, changeAccount){
        console.log(account)
        this.#paginated_data = paginated_data
        this.account = account
        const markup = this.#generateMarkup();
        this.#clearMain();
        this.#main.insertAdjacentHTML('afterbegin', markup);
        this.paginatedData(); // Внутри таблицы
        this.paginateHolding(pagination); //pagination номера страницы
        this.pages = document.querySelectorAll('#pages')
        this.changeChoice(pagination, func, saveHoldingsToTransaction,
             saveHoldingsToHoldings, changeAccount)
        this.sellStocks(saveHoldingsToTransaction, saveHoldingsToHoldings, changeAccount);
    }


    #clearMain() {
        this.#main.innerHTML = '';
    }

    #generateMarkup() {
        return `
        <div class="holdingsPage">
            <div class="holdingsText">
                <h2>Balance: ${this.account.account}$</h1>
                <table style="width:97%" class="holdingsTable">
                    <thead>
                    <tr class="holdings_table_head">
                    <th>ID</th>
                    <th>Company</th>
                    <th>Price(per share)</th>
                    <th>No. of Shares</th>
                    <th>Total Worth</th>
                    <th>Action</th>
                    </thead>
                    <tbody>
                    </tbody>
                </table>

            </div>

            <div class="pagination" id="pagination">
            <a href="#" id="previous_page">&laquo;</a>
            <div class="pagination_page">

            </div>
            <a href="#" id="next_page">&raquo;</a>
            </div>
        </div>
        `
    } 

    paginateHolding(pagination) {
        this.next_page = document.getElementById('next_page')
        this.previous_page = document.getElementById('previous_page')
        let pagination_page = document.querySelector(".pagination_page")


        for(let i = 1; i<=pagination.count; i++){

            pagination_page.innerHTML += `
            <a id="pages" href="#">${i}</a> 
        ` 
        }
    }

    paginatedData(){

        let table = document.getElementsByTagName("tbody")[0]
        table.innerHTML = ''
        for (let i = 0; i < this.#paginated_data.length; ++i) {
            
            let tr = document.createElement('tr');
            
            tr.innerHTML =  `
                    <td>${this.#paginated_data[i].id}</td>
                    <td>${this.#paginated_data[i].title}</td>
                    <td>${this.#paginated_data[i].price_per_share}</td>
                    <td>${this.#paginated_data[i].quantity}</td>
                    <td>${this.#paginated_data[i].total_price}</td> 
                    <td><button class="sell_hold">Продать</button></td>
            `
  
            table.appendChild(tr)
            this.sell_button = document.querySelectorAll(".sell_hold")

        }   
    }

    sellStocks(saveHoldingsToTransaction, saveHoldingsToHoldings, changeAccount){
        
        self = this
        for (let i = 0; i < this.#paginated_data.length; ++i) {
            let self = this
            this.sell_button[i].addEventListener("click", function(){
                
                
                self.data_to_transaction = {
                    title: self.#paginated_data[i].title,
                    symbol: self.#paginated_data[i].symbol,
                    price_per_share: self.#paginated_data[i].price_per_share,
                    action: 'sold',
                    total_price: self.#paginated_data[i].total_price,
                    quantity: self.#paginated_data[i].quantity,
                }
                
                
                self.data_to_holdings = {
                    id: self.#paginated_data[i].id,
                    datetime_deleted: new Date().toISOString().slice(0, 19),
                }
                console.log(self.account.account)
                console.log(self.#paginated_data[i].total_price)
                let account = Number(self.account.account) + Math.trunc(self.#paginated_data[i].total_price * 100) / 100;
                self.account.account = account.toFixed(2)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                saveHoldingsToTransaction(self.data_to_transaction)
                saveHoldingsToHoldings(self.data_to_holdings)
                changeAccount(self.account)
            }) 
            
        }
    }

    changeChoice(pagination, func, saveHoldingsToTransaction, saveHoldingsToHoldings, changeAccount) {
        let self = this;
        let currentPage = 1;

        for(let i = 0; i < pagination.count; i++){
            this.pages[i].setAttribute("page-index", i)
            
        }
        

        this.pages.forEach((button) => {
            
            const pageIndex = Number(button.getAttribute("page-index")) + 1;
            if (pageIndex) {
                button.addEventListener("click", () => {
                    paginated_holding_data(pageIndex);
                    changeClass(button)
                });
            } 
        });

        this.previous_page.addEventListener("click", () => {
            currentPage = currentPage - 1
            if (currentPage == 0) {
                currentPage = 1
                return
            } else{
                paginated_holding_data(currentPage);
                changeClass(this.previous_page)
            }
        });
        
        this.next_page.addEventListener("click", () => {
            currentPage = currentPage + 1
            if (currentPage > pagination.count) {
                currentPage = pagination.count
                return
            } else {
                paginated_holding_data(currentPage);
                changeClass(this.next_page)
            }  
        });

        function changeClass(button) {

            self.pages.forEach((pagNum) => {
                pagNum.classList.remove("active")
                self.next_page.classList.remove("active")
                self.previous_page.classList.remove("active")
            })

            button.classList.add('active');

        }

        function paginated_holding_data(i){
            
            const data = Promise.resolve(func(i));
      
            data.then(value => {
              self.#paginated_data = value

              self.paginatedData(); // Внутри таблицы
              self.sellStocks(saveHoldingsToTransaction, saveHoldingsToHoldings, changeAccount);
              self.pages = document.querySelectorAll('#pages')
             
          
            }).catch(err => {
              console.log(err);
            });
            
        }

    }


}

export default new holdingsView();