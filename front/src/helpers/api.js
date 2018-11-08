import * as axios from 'axios'

import config from '../../config'
import {push_notif_err} from './notifs'

class ApiHelper {
    constructor(){
        this.__backUrl = config.backUrl
        this.__jwtToken = null
    }

    set jwtToken(jwtToken){
        if(jwtToken !== null){
            this.__jwtToken = jwtToken
        }
    }
    get jwtToken(){
        return this.__jwtToken
    }

    checkAuth(){
        let jwtToken = localStorage.getItem('jwtToken');
        if(jwtToken === null){
            // make auth
            return false
        }else{
            this.jwtToken = jwtToken
        }
    }

    get(ressourcePath, params){
        this.checkAuth()
        return new Promise(
            (resolve,reject) => axios.get(
                this.__backUrl + ressourcePath, {
                    params,
                    headers: { 
                        Authorization: `Bearer ${this.jwtToken}`
                    }
                }
            )
            .then((res) => resolve(res.data))
            .catch((err) => push_notif_err(err))
        )
    }
    post(ressourcePath, params){
        this.checkAuth()
        return new Promise(
            (resolve,reject) => axios.post(
                this.__backUrl + ressourcePath, {
                    params,
                    headers: { 
                        Authorization: `Bearer ${this.jwtToken}`
                    }
                }
            )
            .then((res) => resolve(res.data))
            .catch((err) => push_notif_err(err))
        )
    }
    delete(ressourcePath, params){
        this.checkAuth()
        return new Promise(
            (resolve,reject) => axios.delete(
                this.__backUrl + ressourcePath, {
                    params,
                    headers: { 
                        Authorization: `Bearer ${this.jwtToken}`
                    }
                }
            )
            .then((res) => resolve(res.data))
            .catch((err) => push_notif_err(err))
        )
    }
}

export default new ApiHelper()