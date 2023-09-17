
import { API_URL, TIMEOUT_SEC } from "./config.js";
import { timeout } from "./helpers.js";


export let state = {
  get_user: {},
  get_transaction_data: [],
  get_holding_data: [],
  get_stocks_data: {},
  get_holding_pagination: {},
  get_transaction_pagination: {},
  get_paginated_holding_data: {},
  account: {}
};

export let getAccount = async function () {  // для того чтобы получить сумму с БД
  try{  
    let accessToken = localStorage.getItem("access");
    let url = `http://localhost:8000/api/v1/account`
    let response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': 'JWT ' + accessToken
      }
    })
    const res = await Promise.race([response, timeout(TIMEOUT_SEC)]);
    let data = await res.json();
    let account_data = data.results
    
    
    state.account = account_data[0]
    console.log(state.account)
  } catch(err) {
    console.error("Error in model Holding");
  }
}


export let changeAccount = async function(account_data) { // для того чтобы менять счет в БД
  try{    
    
    console.log(account_data)
    let accessToken = localStorage.getItem("access");

    let account_url = `http://localhost:8000/api/v1/account/${account_data.id}`

    const account_response = await fetch(account_url, {
      method: "PATCH", // или 'PUT'
      body: JSON.stringify(account_data), // данные могут быть 'строкой' или {объектом}!
      headers: {
        'Authorization': 'JWT ' + accessToken,
        "Content-Type": "application/json",
      },
    });

    const account_json = await account_response.json();

    console.log("Success you get bank account:", JSON.stringify(account_json));

  } catch(err) {
    console.error("Error in model Holding");
  }
}

export let paginationPage = async function (link = '1') { // // Выгрузка данных пагинации и данных (Пользование пагинации на странице Профиля)
  try{  
    let accessToken = localStorage.getItem("access");
    let url = `http://localhost:8000/api/v1/holding?page=${link}`
    let response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': 'JWT ' + accessToken
      }
    })
    const res = await Promise.race([response, timeout(TIMEOUT_SEC)]);
    let data = await res.json();
    let holding_data = data.results

    const paginated_data = await holding_data.map(holding => {
      return{
        id: holding.id,
        title: holding.title,
        symbol: holding.symbol,
        price_per_share: holding.price_per_share,
        total_price: holding.total_price,
        quantity: holding.quantity,
        date: holding.datetime_created,
        datetime_deleted: holding.datetime_deleted
      }
    })
    
    return paginated_data
  } catch(err) {
    console.error("Error in model Holding");
  }
}

paginationPage()

export let paginationTransactionPage = async function (link = '1') { // Выгрузка данных пагинации и данных (Пользование пагинации на странице Транзакции)
  try{  
    
    let accessToken = localStorage.getItem("access");
    let url = `http://localhost:8000/api/v1/transaction?page=${link}`
    let response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': 'JWT ' + accessToken
      }
    })
    const res = await Promise.race([response, timeout(TIMEOUT_SEC)]);
    let data = await res.json();
    let transaction_data = data.results

    const paginated_data = await transaction_data.map(transaction_data => {
      return{
        id: transaction_data.id,
        title: transaction_data.title,
        symbol: transaction_data.symbol,
        price_per_share: transaction_data.price_per_share,
        total_price: transaction_data.total_price,
        action: transaction_data.action,
        quantity: transaction_data.quantity,
        date: transaction_data.datetime_created,
      }
    })
    
    return paginated_data
  } catch(err) {
    console.error("Error in model Holding");
  }
}

paginationTransactionPage()

export let loadUser = async function () { // для загрузки юзера с БД фото, имени, и.т.д
  try {
    let accessToken = localStorage.getItem("access");

    let id = JSON.parse(atob(accessToken.split(".")[1])).user_id;

    let url = `${API_URL}/auths`;
    let response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: "JWT " + accessToken,
      },
    });

    const res = await Promise.race([response, timeout(TIMEOUT_SEC)]);
    let data = await res.json();
    
    if (!response.ok) throw new Error(`${data.message} (${response.status})`);

    let users = data.results;

    let user = users.map((user) => {
      if (user.id === id) {
        state.get_user = {
          user_name: user.user_name,
          first_name: user.first_name,
          last_name: user.last_name,
          email: user.email,
          image_url: user.image_url,
        };
        return user;
      }

    
    });
    
  } catch (err) {
    alert(err);
    console.error("Error in model load user");
  }
};


export let postRegisterData = async function(formUser) { // отправить данные в Сервер для регистрации юзера
  try{
    let xhr = new XMLHttpRequest();
    xhr.open("POST", `${API_URL}/auths`)
    
    
    
    formUser.addEventListener('submit', (data) => {
      let jsonForm = new FormData(formUser);
      
      data.preventDefault();
      
      xhr.responseType = 'json'
      xhr.send(jsonForm);
      xhr.onload = (res) => {
          if(xhr.status != 200){
              console.error(`Something went wrong ${xhr.status}: ${xhr.statusText}`);
          } else{
              location.href = '../index.html'
          }
      }
  })

  } catch(err) {
    console.error("Error in model register");
  }
}

export let loginUser = async function(formUser) { // отправить данные в Сервер для логина юзера
  try{
    let xhr = new XMLHttpRequest();
    xhr.open("POST", `${API_URL}/token/`)
    
    formUser.addEventListener('submit', (data) => {
        
        let jsonForm = new FormData(formUser);
        
        data.preventDefault();
        
        xhr.responseType = 'json'
        xhr.send(jsonForm);
        xhr.onload = (res) => {
            if(xhr.status != 200){
                console.error(`Something went wrong ${xhr.status}: ${xhr.statusText}`);
                
            } else{
                localStorage.setItem('access', xhr.response.access)
                localStorage.setItem('refresh', xhr.response.refresh)

                showAboutSite();
            }
        }
    })
  }
  catch(err) {
    console.error("Error in model login");
  }
}


export let getStocksApi = async function() {  // Получить API акции компании для каталога 
  try {
    let url = 'https://gist.githubusercontent.com/stevekinney/f96d5800852e91282f46/raw/ea047c2f5898de6c9fecf535db8b30abcfe5b423/stocks.json'
    let response = await fetch(url, {
      method: 'GET',
    })
    const res = await Promise.race([response, timeout(TIMEOUT_SEC)]);
    let data = await res.json();
    
    state.get_stocks_data = data.map(stocks => {
      return{
        title: stocks.company,
        description: stocks.description,
        price_per_share: stocks.initial_price,
        symbol: stocks.symbol
      }
    })
    
  } 
  catch(err) {
    console.error("Error in model login" + err);
  }
}

export let getTransactionData = async function() { // Получить данные с БД (Транзакции)
  try{
    let accessToken = localStorage.getItem("access");
    let url = 'http://localhost:8000/api/v1/transaction'
    let response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': 'JWT ' + accessToken
      }
    })

    const res = await Promise.race([response, timeout(TIMEOUT_SEC)]);
    let data = await res.json();
    const transaction = data.results;
    const transactionPagination = data.pagination

    state.get_transaction_pagination =  {
      count: transactionPagination.count,
      next: transactionPagination.next,
      previous: transactionPagination.previous
    }

    state.get_transaction_data = transaction.map(transaction => {
      return{
        id: transaction.id,
        title: transaction.title,
        symbol: transaction.symbol,
        price_per_share: transaction.price_per_share,
        total_price: transaction.total_price,
        action: transaction.action,
        quantity: transaction.quantity,
        date: transaction.datetime_created,
      }
    })


  }
  catch(err) {
    console.error("Error in model login");
  }
}


export let getHoldingData = async function() {  // Получить данные с БД (Профиль)
  try{
    let accessToken = localStorage.getItem("access");
    let url = 'http://localhost:8000/api/v1/holding'
    let response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': 'JWT ' + accessToken
      }
    })

    const res = await Promise.race([response, timeout(TIMEOUT_SEC)]);
    let data = await res.json();
    const holding = data.results;
    const holding_pagination = data.pagination


    state.get_holding_pagination =  {
        count: holding_pagination.count,
        next: holding_pagination.next,
        previous: holding_pagination.previous
      }
    
    state.get_holding_data = holding.map(holding => {
      return{
        id: holding.id,
        title: holding.title,
        symbol: holding.symbol,
        price_per_share: holding.price_per_share,
        total_price: holding.total_price,
        quantity: holding.quantity,
        date: holding.datetime_created,
      }
    })
    
  }
  catch(err) {
    console.error("Error in model login" + err);
  }
}


export let saveHoldingTransaction = async function(holding_data, transaction_data) { // сохранение данных в БД по проф и транзакц (При покупке)
  try{    
    let accessToken = localStorage.getItem("access");
    let holding_url = 'http://localhost:8000/api/v1/holding'
    let transaction_url = 'http://localhost:8000/api/v1/transaction'

    const holding_response = await fetch(holding_url, {
      method: "POST", // или 'PUT'
      body: JSON.stringify(holding_data), // данные могут быть 'строкой' или {объектом}!
      headers: {
        'Authorization': 'JWT ' + accessToken,
        "Content-Type": "application/json",
      },
    });

    const transaction_response = await fetch(transaction_url, {
      method: "POST", // или 'PUT'
      body: JSON.stringify(transaction_data), // данные могут быть 'строкой' или {объектом}!
      headers: {
        'Authorization': 'JWT ' + accessToken,
        "Content-Type": "application/json",
      },
    });

    Promise.all([holding_response, transaction_response])

    const holding_json = await holding_response.json();
    const transaction_json = await transaction_response.json();
    
    console.log("Успех:", JSON.stringify(holding_json));
    console.log("Success:", JSON.stringify(transaction_json));
  } catch(err) {
    console.error("Error in model Holding");
  }
}

export let saveHoldingsToTransaction = async function(transaction_data) { // сохранение данных в транзакциях при продаже (Профиль)
  try{    
    
    let accessToken = localStorage.getItem("access");

    let transaction_url = `http://localhost:8000/api/v1/transaction`

    const transaction_response = await fetch(transaction_url, {
      method: "POST", // или 'PUT'
      body: JSON.stringify(transaction_data), // данные могут быть 'строкой' или {объектом}!
      headers: {
        'Authorization': 'JWT ' + accessToken,
        "Content-Type": "application/json",
      },
    });

    const transaction_json = await transaction_response.json();

    console.log("Success:", JSON.stringify(transaction_json));

  } catch(err) {
    console.error("Error in model Holding");
  }
}

export let saveHoldingsToHoldings = async function(holding_data) { // Удаление данных с БД при продаже акции (Профиль)
  try{    
    
    let accessToken = localStorage.getItem("access");

    let holding_url = `http://localhost:8000/api/v1/holding/${holding_data.id}`

    const holding_response = await fetch(holding_url, {
      method: "DELETE", // или 'PUT'
      body: JSON.stringify(holding_data), // данные могут быть 'строкой' или {объектом}!
      headers: {
        'Authorization': 'JWT ' + accessToken,
        "Content-Type": "application/json",
      },
    });

    const holding_json = await holding_response.json();

    console.log("Success:", JSON.stringify(holding_json));

  } catch(err) {
    console.error("Error in model Holding");
  }
}
