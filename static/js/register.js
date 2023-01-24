export default {
    data() {
        return {
            welcome: 'Нет учётки? Зарегистрируйтесь!',
            username: '',
            email: '',
            password: '',
            register_errors: ''
        }
    },
    methods: {
        async register_submit(e) {
            const requestOptions = {
                method: "POST",
                headers: {"Content-Type": "application/json" },
                body: JSON.stringify({
                    "username": this.username,
                    "email": this.email,
                    "password": this.password
                })
            }
            
            const response = await fetch('/api/v1/register/', requestOptions)

            const response_json = await response.json()
            if (response['status'] != 201) {
                this.register_errors = Object.values(response_json)
                return
            }
            this.$router.push('/login')
        }
    },
    template: `
    <form @submit.prevent="register_submit">
        <p>{{ welcome }}</p>

        <div v-if="register_errors">
            <div v-for="error in register_errors" :key="error.id">
                <small v-for="error_part in error" :key="error_part.id" class="text-primary">
                    {{ error_part }}
                </small>
            </div>
        </div>

        <input v-model="username" class="form-control mb-2" placeholder="Имя" required>
        <input v-model="email" type="email" class="form-control mb-2" placeholder="Почта" required>
        <input v-model="password" type="password" class="form-control mb-4" placeholder="Пароль" required>
        <input type="submit" class="form-control btn btn-outline-info" value="Зарегистрироваться">
    </form>
    `
}