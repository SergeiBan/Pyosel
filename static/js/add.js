export default {
    data() {
        return {
            city: null,
            parent: null,
            species: 'dogs',
            gender: 'M',
            
            accessories: null,
            breed: null,
            features: null,
            hue: null,
            size: null,
            status: this.$route.path.split('_')[1],
            avatar: null,
            auxPhoto: null,
            avatar_url: null,
            auxPhoto_url: null,

            city_part: null,
            street: null,
            date: null,

            
            nickname: null,
            age: null,
            bounty: null,

            token: window.localStorage.getItem('token'),
            errors: null
        }
    },
    methods: {
        async add_submit(e) {

            let data = new FormData()
            data.append('city', this.city)
            data.append('species', this.species)
            data.append('gender', this.gender)
            data.append('status', this.status)
            data.append('size', this.size)
            data.append('accessories', this.accessories)
            data.append('breed', this.breed)
            data.append('features', this.features)
            data.append('hue', this.hue)
            data.append('avatar', this.avatar)
            data.append('aux_photo', this.auxPhoto)

            const requestOptions = {
                method: "POST",
                headers: {"Authorization": `Token ${this.token}`},
                body: data
            }
            const response = await fetch('/api/v1/animals/', requestOptions)
            const responseJson = await response.json()
            if (response['status'] != 201) {
                this.errors = Object.values(responseJson)
                return
            }

            if (this.status === 'lost') {
                const dataLost = JSON.stringify({
                    animal: responseJson['pk'],
                    nickname: this.nickname,
                    loss_city_part: this.city_part,
                    loss_street: this.street,
                    loss_date: this.date,
                    bounty: this.bounty
                })

                const requestOptionsLost = {
                    method: "POST",
                    headers: {"Authorization": `Token ${this.token}`, 'Content-Type': 'application/json'},
                    body: dataLost
                }

                const responseLost = await fetch('/api/v1/lost_profiles/', requestOptionsLost)
                const responseLostJson = await responseLost.json()
                if (responseLost['status'] != 201) {
                    this.errors = Object.values(responseLostJson)
                    return
                }
            }

            if (this.status === 'found') {
                const dataFound = JSON.stringify({
                    animal: responseJson['pk'],
                    found_city_part: this.city_part,
                    found_street: this.street,
                    found_date: this.date,
                })

                const requestOptionsFound = {
                    method: "POST",
                    headers: {"Authorization": `Token ${this.token}`, 'Content-Type': 'application/json'},
                    body: dataFound
                }

                const responseFound = await fetch('/api/v1/found_profiles/', requestOptionsFound)
                const responseFoundJson = await responseFound.json()
                if (responseFound['status'] != 201) {
                    this.errors = Object.values(responseFoundJson)
                    return
                }
            }
            const redirect_url = this.status === 'lost' ? 'found' : 'lost'
            this.$router.push(redirect_url)
            
        },
        add_photos(event) {
            console.log(this.status)
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
                  if (fieldName == 'avatar') { this.avatar_url = url_cropped; this.avatar = file; }
                  if (fieldName == 'aux_photo') { this.auxPhoto_url = url_cropped; this.auxPhoto = file }
                  console.log(this.auxPhoto_url)
        
                }, img_data.type, 0.3);
            });
        }
    },
    template: `
    <form @submit.prevent="add_submit" enctype="multipart/form-data">
        <div v-if="errors">
            <div v-for="error in errors" :key="error.id">
                <small v-for="error_part in error" :key="error_part.id" class="text-primary">
                    {{ error_part }}
                </small>
            </div>
        </div>

        <h2>???????????????????????? ????????</h2>
        <p>?????????????? ??????????????</p>

        <select v-model="species" class="form-select mb-2" required>
            <option value="dogs">????????????</option>
            <option value="cats">??????????</option>
        </select>

        <select v-model="gender" class="form-select mb-2" required>
            <option value="M">??</option>
            <option value="F">??</option>
        </select>

        <input v-model="city" class="form-control mb-2" placeholder="??????????" required>
        <input v-model="date" class="form-control mb-2" placeholder="????????" type="date">

        <input v-if="status === 'lost'" v-model="nickname" class="form-control mb-4" placeholder="????????????" required>

        <h2>???????????????????????????? ????????</h2>
        <input v-if="status === 'lost'" v-model="bounty" class="form-control mb-4" placeholder="?????????????? ???, ???????? ????????">

        <p class="my-2">??????
            <span v-if="status === 'found'">??????????????</span>
            <span v-if="status === 'lost'">??????????????????</span> ???????????????
        </p>

        <input v-model="city_part" class="form-control mb-2" placeholder="??????????/?????????? ????????????">
        <input v-model="street" class="form-control mb-2" placeholder="??????????">

        <p>??????????????????????</p>
        <input v-model="size" class="form-control mb-2" placeholder="????????????" type="text">
        <input v-model="accessories" class="form-control mb-2" placeholder="????????????????????" type="text">
        <input v-model="breed" class="form-control mb-2" placeholder="????????????" type="text">
        <input v-model="features" class="form-control mb-2" placeholder="??????????????" type="text" maxlength="2000">
        <input v-model="hue" class="form-control mb-2" placeholder="??????????" type="text">

        <div class="row">
            <div class="col-md-6">
                <label for="avatar">?????????????? ????????</label>
                <input id="avatar" type="file" accept="image/*" @change="add_photos" class="form-control mb-2" name="avatar">
                <img v-if="avatar_url" :src="avatar_url" alt="???????????????? ???????????????? ????????" class="img-fluid img-thumbnail">
            </div>
            <div class="col-md-6">
                <label for="auxiliary">???????????????????????????? ????????</label>
                <input id="auxiliary" type="file" accept="image/*" @change="add_photos" class="form-control mb-2" name="aux_photo">
                <img v-if="auxPhoto_url" :src="auxPhoto_url" alt="???????????????????????? ?????????????????????????????? ????????" class="img-fluid img-thumbnail">
            </div>
        </div>

        <div style="position: absolute; top: 15px;">
            <div id="image-box" class="image-container"></div>
            <button class="btn btn-info" id="crop-btn" style="width: 100%; margin-top: 10px; display: none;" type="button">????????????????</button>  
        </div>
        
        <button class="btn btn-outline-info" id="confirm-btn" style="width: 100%; margin-top: 10px;" type="submit">????????????????</button>
        <!-- <input type="submit" class="form-control btn btn-outline-info" value="????????????????"> -->
    </form>
    `
}