export default {
    data() {
        return {
            welcome: 'Опишите животное',
            city: '',
            parent: '',
            species: '',
            name: '',
            breed: '',
            description: '',
            color: '',
            on_sale: '',
            price: '',
            free_to_take: '',
            lost: '',
            found: '',
            photos: '',
            token: window.localStorage.getItem('token'),
            errors: ''
        }
    },
    methods: {
        async add_submit(e) {
            
            let data = new FormData()
            data.append('city', this.city)
            data.append('species', this.species)
            data.append('name', this.name)
            data.append('avatar', Array.from(this.photos)[0])

            const requestOptions = {
                method: "POST",
                headers: {"Authorization": `Token ${this.token}`},
                body: data
                // body: JSON.stringify({
                //     "city": this.city,
                //     "species": this.species,
                //     "name": this.name,
                //     "photos": this.photos
                // })
            }
            
            const response = await fetch('/api/v1/animals/', requestOptions)
            
            const response_json = await response.json()
            console.log(response_json)

            if (response['status'] != 200) {
                this.login_errors = Object.values(response_json)
            } else {
                this.$router.push('/')
            }
            
        },
        add_photos(event) {
            this.photos = event.target.files
        }
    },
    template: `
    <form @submit.prevent="add_submit">
        <p>{{ welcome }}</p>

        <div v-if="errors">
            <div v-for="error in errors" :key="error.id">
                <small v-for="error_part in error" :key="error_part.id" class="text-primary">
                    {{ error_part }}
                </small>
            </div>
        </div>

        <h2>Обязательные поля</h2>
        <input v-model="city" class="form-control mb-2" placeholder="Город" required>
        <select v-model="species" class="form-select mb-2" required>
            <option disabled value="">Категория</option>
            <option value="dogs">Собаки</option>
            <option value="cats">Кошки</option>
        </select>
        <input v-model="name" class="form-control mb-4" placeholder="Кличка" required>

        <h2>Необязательные поля</h2>
        <input type="file" accept="image/*" name="file-1" @change="add_photos" class="form-control mb-2">
        <input type="file" name="file-2" class="form-control mb-2">
        <input type="file" name="file-3" class="form-control mb-2">
        <input type="file" name="file-4" class="form-control mb-2">
        <input type="file" name="file-5" class="form-control mb-2">
        <input type="submit" class="form-control btn btn-outline-info" value="Добавить">
    </form>
    `
}