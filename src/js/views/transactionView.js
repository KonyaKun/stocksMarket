class transactionView{
    #main = document.querySelector(".main");
    #paginated_data;
    #account;
    data_to_transaction;
    next_page;
    previous_page;
    pages;

    render(paginated_data, pagination, func, account){
        
        this.#paginated_data = paginated_data
        this.#account = account.account
        
        const markup = this.#generateMarkup();
        this.#clearMain();
        this.#main.insertAdjacentHTML('afterbegin', markup);
        this.paginatedData(); // Внутри таблицы
        this.paginateHolding(pagination); //pagination номера страницы
        this.pages = document.querySelectorAll('#pages')
        
        this.#changeChoice(pagination, func)
    }

    #clearMain() {
        this.#main.innerHTML = '';
    }

    #generateMarkup() {
        return `

        <div class="transactionPage">
            <div class="transactionText">
                <h2>Balance: ${this.#account}$</h1>
                <table style="width:97%">
                    <thead>
                        <tr class="transaction_table_head">
                            <th>Transaction id</th>
                            <th>Company</th>
                            <th>Bought/Sold</th>
                            <th>Price(per share)</th>
                            <th>No. of Shares</th>
                            <th>Total price</th>
                        </tr> 
                    </thead>                  
                    <tbody>
                    </tbody>           
                </table>

                <div class="pagination" id="pagination">
                    <a href="#" id="previous_page">&laquo;</a>
                <div class="pagination_page">
        
                </div>
                    <a href="#" id="next_page">&raquo;</a>
                </div>
            </div>
        </div>
    `
    } 


    paginatedData(){

        let table = document.getElementsByTagName("tbody")[0]
        table.innerHTML = ''
        for (let i = 0; i < this.#paginated_data.length; ++i) {
            let tr = document.createElement('tr');
            
            tr.innerHTML =  `
                    <td>${this.#paginated_data[i].id}</td>
                    <td>${this.#paginated_data[i].title}</td>
                    <td>${this.#paginated_data[i].action}</td>
                    <td>${this.#paginated_data[i].price_per_share}</td>
                    <td>${this.#paginated_data[i].quantity}</td>
                    <td>${this.#paginated_data[i].total_price}</td> 
        
                `
  
            table.appendChild(tr)
            
        }   
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

    #changeChoice(pagination, func) {
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
              self.sell_button = document.querySelector(".sell_hold")
              self.pages = document.querySelectorAll('#pages')
          
            }).catch(err => {
              console.log(err);
            });
            
          }

    }
}

export default new transactionView();

