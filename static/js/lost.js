export default {
    data() {
        return {
            profiles: null,
            url: '/api/v1/lost_profiles/',
            city: null,
            date: null
        }
    },
    methods: {
        async detailsSubmit(e) {
            if (this.date === null || this.city === null) { return }
            const requestOptions = { method: "GET" }
            const response = await fetch(`${this.url}?city=${this.city}&date=${this.date}`, requestOptions)
            this.profiles = await response.json()
        }
    },
    template: `
    <div class="col-md-6">
        <input v-model="city" type="text" placeholder="Город" class="form-control mb-4" @blur="detailsSubmit">
    </div>
    <div class="col-md-6">
        <input v-model="date" type="date" class="form-control mb-4" @blur="detailsSubmit">
    </div>
    <div v-for="profile in profiles" :key="profile.id" class="card col-md-6 col-xl-3">
        <img :src="profile.animal.avatar_thumbnail" class="card-img-top" alt="Фото животного">
        <div class="card-body text-center">
            <h5 class="card-title">
                <span class="badge bg-info">{{ profile.animal.nickname }}</span>{{ profile.animal.city }}
            </h5>
            <p class="card-text">{{ profile.animal.nickname }}</p>
        </div>
    </div>
    
    `
    
}