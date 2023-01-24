export default {
    data() {
        return {
            welcome: 'Опишите животное',
            city: null,
            parent: null,
            species: null,
            name: null,
            breed: null,
            description: null,
            color: null,
            on_sale: null,
            price: null,
            free_to_take: null,
            lost: null,
            found: null,
            photos: [],
            avatar_url: null,
            aux_1_url: null,
            aux_2_url: null,
            token: window.localStorage.getItem('token'),
            errors: null
        }
    },
    methods: {
        async add_submit(e) {
            let data = new FormData()
            data.append('city', this.city)
            data.append('species', this.species)
            data.append('name', this.name)
            data.append('images', this.photos[0])
            data.append('images', this.photos[1])

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
            this.photos.push(event.target.files[0])
            const fieldName = event.target.name
            if (fieldName == 'avatar') { this.avatar_url = URL.createObjectURL(event.target.files[0])}
            if (fieldName == 'aux-1') { this.aux_1_url = URL.createObjectURL(event.target.files[0])}
            if (fieldName == 'aux-2') { this.aux_2_url = URL.createObjectURL(event.target.files[0])}
        }
    },
    template: `
    <form @submit.prevent="add_submit" enctype="multipart/form-data">
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
        <div class="row">
            <div class="col-md-4">
                <label for="avatar">Главное фото</label>
                <input id="avatar" type="file" accept="image/*" @change="add_photos" class="form-control mb-2" name="avatar">
                <img v-if="avatar_url" :src="avatar_url" alt="Просмотр главного фото" class="img-fluid img-thumbnail">
            </div>
            <div class="col-md-4">
                <label for="auxiliary-1">Вспомогательное фото</label>
                <input id="auxiliary-1" type="file" accept="image/*" @change="add_photos" class="form-control mb-2" name="aux-1">
                <img v-if="aux_1_url" :src="aux_1_url" alt="Просмотр дополнительного фото" class="img-fluid img-thumbnail">
            </div>
            <div class="col-md-4">
                <label for="auxiliary-2">Вспомогательное фото</label>
                <input id="auxiliary-2" type="file" accept="image/*" @change="add_photos" class="form-control mb-2" name="aux-2">
                <img v-if="aux_2_url" :src="aux_2_url" alt="Просмотр дополнительного фото" class="img-fluid img-thumbnail">
            </div>
        </div>
        <input type="submit" class="form-control btn btn-outline-info" value="Добавить">
    </form>
    `
}