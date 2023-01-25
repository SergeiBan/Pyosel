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
            const img_data = event.target.files[0]
            
            const fieldName = event.target.name
            const fieldId = event.target.id
            const img_url = URL.createObjectURL(img_data)

            const imagebox = document.getElementById('image-box')
            const crop_btn = document.getElementById('crop-btn')
            const inputField = document.getElementById(fieldId)

            imagebox.innerHTML = `<img src="${ img_url }" id="image" style="width:100%;"></img>`
            const image = document.getElementById('image')
            
            document.getElementById('image-box').style.display = 'block'
            document.getElementById('crop-btn').style.display = 'block'
            document.getElementById('confirm-btn').style.display = 'none'

            const cropper = new Cropper(image, {
                aspectRatio: 1 / 1,
                autoCropArea: 1,
                viewMode: 1,
                scalable: false,
                zoomable: false,
                movable: false,
                minCropBoxWidth: 200,
                minCropBoxHeight: 200,
            })

            crop_btn.addEventListener('click', ()=>{
                cropper.getCroppedCanvas().toBlob((blob)=>{
                  
                  let file = new File([blob], img_data.name,{type:"image/*", lastModified:new Date().getTime()});
                  let container = new DataTransfer();
                  container.items.add(file);
                  inputField.files = container.files;
        
                  document.getElementById('image-box').style.display = 'none'
                  document.getElementById('crop-btn').style.display = 'none'
                  document.getElementById('confirm-btn').style.display = 'block'

                  const url_cropped = URL.createObjectURL(file)
                  this.photos.push(file)
                  if (fieldName == 'avatar') { this.avatar_url = url_cropped }
                  if (fieldName == 'aux-1') { this.aux_1_url = url_cropped }
                  if (fieldName == 'aux-2') { this.aux_2_url = url_cropped }
        
                }, img_data.type, 0.7);
            });
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

        <div style="position: absolute; top: 15px;">
            <div id="image-box" class="image-container"></div>
            <button class="btn btn-info" id="crop-btn" style="width: 100%; margin-top: 10px; display: none;" type="button">Образать</button>  
        </div>
        
        <button class="btn btn-outline-info" id="confirm-btn" style="width: 100%; margin-top: 10px;" type="submit">Post</button>
        <!-- <input type="submit" class="form-control btn btn-outline-info" value="Добавить"> -->
    </form>
    `
}