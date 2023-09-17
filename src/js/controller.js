import 'core-js/stable'
import * as model from "./model.js";
import userView from './views/userView.js';
import aboutView from './views/aboutView.js'
import registerView from './views/registerView.js'
import loginView from './views/loginView.js'
import aboutCompanyViews from './views/aboutCompanyViews.js';
import transactionView from './views/transactionView.js';
import catalogView from './views/catalogView.js';
import holdingsViews from './views/holdingsViews.js';
import stockCardView from './views/stockCardView.js';


const showUser = async function () { // для показа юзера
  try {
    // 1) Загрузка Юзера с БД

    await model.loadUser();
    
    // 2) Отображение Юзера на странице
    userView.render(model.state.get_user);

  } catch (err) {
    alert(err);
    console.error("Something doesn't work in Controller");
  }
};


showAboutSite = async function() { // страница о сайте
  try{
      window.location.hash = 'aboutSite';
      // 1) Загрузка Юзера с БД
      await model.loadUser();
      let user = model.state.get_user.user_name
      // 2) Загрузка страницы о сайте
      aboutView.render(user)
  } catch(err) {
      console.error(err); 
  }
}



showRegister = async function() { // страница регистрации
  try{
    window.location.hash = 'register';
    // 1) Загрузка страницы регистрации
    registerView.render();
    // 2) Загрузка данных регистрации (введеных) в БД
    model.postRegisterData(registerView.userForm);

  } catch(err) {
    console.error(err);
  }
}


showLogin = async function() { // страница логина
  try{
    window.location.hash = 'login';
    // 1) Загрузка страницы логина
    loginView.render();
    // 2) Загрузка данных логинформы (введеных) в БД
    model.loginUser(loginView.formUser);

  } catch(err) {
    console.error(err);
  }
}

showAboutCompany = async function() {  // страница о компании 
  try {

    window.location.hash = 'aboutCompany';
    // 1) Загрузка страницы о Компании(нашего сайта)
    aboutCompanyViews.render();
    
  }
  catch(err) {
    console.error(err);
  }
}



showTransaction = async function() {  // страница транзакции
  try {
    window.location.hash = 'transaction';
    // 1) Загрузкa данных транзакции с БД
    model.getTransactionData()
    let paginated_transaction_data = await model.paginationTransactionPage()
    // 2) Загрузка страницы о транзакции 
    transactionView.render(paginated_transaction_data, model.state.get_transaction_pagination, model.paginationTransactionPage, model.state.account);
    
  }
  catch(err) {
    console.error(err);
  }
}


showHoldings = async function() { // страница ваших акции профиль
  try {
 
    window.location.hash = 'holdings';
    let hash = window.location.hash
    
    if(hash == '#holdings' ){
      // 1) Загрузкa данных профиля с БД
      await model.getHoldingData()
      // 2) Загрузкa данных банковского счета с БД
      await model.getAccount()
      // 3) Загрузкa данных пагинации профиля с БД
      let paginated_data = await model.paginationPage()
      // 4) Загрузкa данных пагинации с модели
      let holding_pagination_numb = model.state.get_holding_pagination
      
      // 5) Загрузкa страницы о профиле 
      holdingsViews.render(paginated_data, holding_pagination_numb, model.paginationPage, 
      model.saveHoldingsToTransaction, model.saveHoldingsToHoldings, 
      model.state.account, model.changeAccount);
    } 
  }
  catch(err) {
    console.error(err);
  }
}



showCatalogCompany = async function() { // страница показ Компаний
  try {

    window.location.hash = 'catalog';
    // 1) Загрузкa данных о компаниях API с другого ресурса
    await model.getStocksApi()
    // 2) Загрузкa страницы о каталоге компании 
    catalogView.render(model.state.get_stocks_data);
    
  }
  catch(err) {
    console.error(err);
  }
}


showCardCompany = async function() { // показ карточки компании
  try{

    window.location.hash = 'company'
    // 1) Берем названия компании, для того чтобы вытащить выбранную компанию в карточке 
    let company_title = event.target.value
    // 2) Загрузкa данных о счета с БД
    await model.getAccount()
    // 3) Загрузкa данных о компаниях API с другого ресурса
    await model.getStocksApi()
    // 4) Загрузкa страницы о карточке компании
    stockCardView.render(model.state.get_stocks_data, 
      company_title, model.state.account, model.saveHoldingTransaction, model.changeAccount)     
    
  }
  catch(err) {
    console.error(err)
  }
}





const init = function() {
  showUser()
  let hash = window.location.href.slice(22);
  if(hash == '#aboutSite'){
    showAboutSite()
  } else if(hash == '#aboutCompany'){
    showAboutCompany()
  } else if(hash == '#transaction'){
    showTransaction()
  } else if(hash == '#holdings'){
    showHoldings()
  } else if(hash == '#catalog'){
    showCatalogCompany()
  } else if(hash == '#company'){
    showCardCompany()
  } 
}

let user = localStorage.getItem("access")
if(user) {
  init()
} else{
  showAboutSite()
}
