
class loginView {
    #main = document.querySelector(".main");
    formUser;

    render(){
        const markup = this.#generateMarkup();
        this.#clearMain();
        this.#main.insertAdjacentHTML('afterbegin', markup);
        this.formUser = document.forms.login;
    }


    #clearMain() {
        this.#main.innerHTML = '';
    }

    #generateMarkup() {
        return `
        <form 
            action="#" 
            method="post" 
            id="login" 
            name="login"
            class="form"
        >
            <h1 class="sign">Авторизация</h1>
            <input type="text" id="user_name" name="user_name" placeholder="Login">
            <input type="password" name="password" id="password" placeholder="Password">
            <input type="submit" value="Sign in" class="submit">
        </form>
        `
    } 
}

export default new loginView();