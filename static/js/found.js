export default {
    data() {
        return {
            profiles: null,
            found_url: '/api/v1/found_profiles/'
        }
    },
    props: {
        city: String
    },
    async mounted() {
        const requestOptions = { method: "GET" }
        const response = await fetch(this.found_url, requestOptions)
        this.profiles = await response.json()
    },
    template: `
    <div v-for="profile in profiles" :key="profile.id" class="card col-md-6 col-xl-3">
        <img :src="profile.animal.avatar_thumbnail" class="card-img-top" alt="Фото животного">
        <div class="card-body text-center">
            <h5 class="card-title"><span class="badge bg-info">{{ profile.animal.status }}</span>{{ profile.animal.city }}</h5>
        </div>
    </div>
    
    `
    
}