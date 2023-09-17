import * as img from '../../../tradingStocks/media/images/*'
import quit from '../../../src/img/quit.png'

class userView {
    #authmark = document.querySelector('.authorization')
    #data;
    #images;


    render(data){
        this.#data = data;
        const omg = img[this.#data.image_url.slice(28)]
        this.#images = new URL(omg, import.meta.url)
        const markup = this.#generateMarkup();
        this.#clearUser();
        this.#authmark.insertAdjacentHTML('afterbegin', markup);
        this.#userExit();
    }


    #clearUser() {
        this.#authmark.innerHTML = '';
    }


    #generateMarkup() {
        return `
          <div class="user_icon">
          <img src="${this.#images.href}" type="image/jpeg" alt="user_image" >
          <p>${this.#data.user_name}</p>
          </div>
          <button class="userBtn"><img src="${quit}"></button>
        `
    }

    
    #userExit(){
        let btn = document.querySelector('.userBtn')
        btn.addEventListener('click', function (){
          localStorage.removeItem("access")
          localStorage.removeItem("refresh")
          location.reload()
        })
    }
}


export default new userView();