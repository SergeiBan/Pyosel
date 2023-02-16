export default {
    data() {
        return {
            animals: null,
            url: '/api/v1/animals/'
        }
    },
    props: {
        city: String
    },
    methods: {
        async detailsSubmit(e) {
            if (this.date === null || this.city === null) { return }
            const requestOptions = { method: "GET" }
            const response = await fetch(`${this.url}?city=${this.city}&date=${this.date}&species=${this.species}&gender=${this.gender}`, requestOptions)
            this.profiles = await response.json()
        }
    },
    mounted: {

    },
    template: `
    <div class="col-12"><p>Пожалуйста, уточните, какого питомца вы потеряли? Где и когда?
        Вслед за этим будут показаны все подходящие найденные животные.</p></div>
    <div class="col-md-3">
        <input type="text" v-model="city" placeholder="Город" class="form-control mb-4" @blur="detailsSubmit">
    </div>
    <div class="col-md-3">
        <input type="date" v-model="date" class="form-control mb-4" @blur="detailsSubmit">
    </div>
    <div class="col-md-3">
        <select v-model="species" class="form-select mb-2" required @blur="detailsSubmit">
            <option value="dogs">Собаки</option>
            <option value="cats">Кошки</option>
        </select>
    </div>
    <div class="col-md-3">
        <select v-model="gender" class="form-select mb-2" required @blur="detailsSubmit">
            <option value="M">М</option>
            <option value="F">Ж</option>
        </select>
    </div>
    <div v-for="profile in profiles" :key="profile.id" class="card col-md-6 col-xl-3">
        <img :src="profile.animal.avatar_thumbnail" class="card-img-top" alt="Фото животного">
        <div class="card-body text-center">
            <h5 class="card-title"><span class="badge bg-info">{{ profile.found_date }}</span></h5>
            <p class="card-text>
            {{ profile.animal.gender }}
            {{ profile.city_part }} {{ profile.city_st</p>
        </div>
    </div>
    
    `
    
}