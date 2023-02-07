export default {
    data() {
        return {
            profiles: null,
            url: '/api/v1/lost_profiles/'
        }
    },
    props: {
        city: String
    },
    async mounted() {
        const requestOptions = { method: "GET" }
        const response = await fetch(this.url, requestOptions)
        this.profiles = await response.json()
    },
    template: `
    <div v-for="profile in profiles" :key="profile.id" class="card col-md-6 col-xl-3">
        <img :src="profile.animal.avatar_thumbnail" class="card-img-top" alt="Фото животного">
        <div class="card-body text-center">
            <h5 class="card-title">
                <span class="badge bg-info">{{ profile.animal.nickname }}</span>{{ profile.animal.city }}
            </h5>
            <p class="card-text">{{ profile.animal }}
            </p>
        </div>
    </div>
    
    `
    
}