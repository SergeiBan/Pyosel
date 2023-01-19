export default {
    data() {
        return {
            welcome: 'Введите имя и пароль для входа',
            username: '',
            password: '',
            login_errors: ''
        }
    },
    methods: {
        async login_submit(e) {
            const requestOptions = {
                method: "POST",
                headers: {"Content-Type": "application/json" },
                body: JSON.stringify({
                    "username": this.username,
                    "password": this.password
                })
            }
            
            const response = await fetch('/api/v1/login/', requestOptions)
            const response_json = await response.json()
            console.log(response, '\n', response_json)

            if (response['status'] != 200) {
                this.login_errors = Object.values(response_json)
            } else {
                window.localStorage.setItem('token', response_json['token'])
                window.localStorage.setItem('token_expiry', response_json['expiry'])
                this.$emit('login', true)
                this.$router.push('/')
            }
            
        }
    },
    template: `
    <form @submit.prevent="login_submit">
        <p>{{ welcome }}</p>

        <div v-if="login_errors">
            <div v-for="error in login_errors" :key="error.id">
                <small v-for="error_part in error" :key="error_part.id" class="text-primary">
                    {{ error_part }}
                </small>
            </div>
        </div>

        <input v-model="username" class="form-control mb-2" placeholder="Имя" required>
        <input v-model="password" type="password" class="form-control mb-4" placeholder="Пароль" required>
        <input type="submit" class="form-control btn btn-outline-info" value="Войти">
    </form>
    `
}