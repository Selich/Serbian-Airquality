import Geolocation from 'Geolocation';

class Locator {
    getCity(success, failure) {
        return this.getPosition(
            (position) => {
                this.parseCoords(position.coords.longitude, position.coords.latitude, (result) => {
                    success(result);
                }, (error) => {
                    failure(error);
                });
            },
            (error) => {
                failure(error);
            }
        );
    }

    getPosition(success, failure) {
        return Geolocation.getCurrentPosition(
            (position) => {
                console.log(position.coords);
                success(position);
            },
            (error) => {
                failure(error);
                console.log('Failed to get current position');
            },{
                enableHighAccuracy: false,
                timeout: 20000,
                maximumAge: 1,
                //maximumAge: 43200000,
            });
    }

    parseCoords(longitude, latitude, success, failure) {
        console.log(longitude + '' + latitude);
        return fetch(this.getURLByCoords(longitude, latitude))
            .then((response) => response.json())
            .then((responseJson) => {
                console.log(responseJson);

                if(responseJson.status !== '1') {
                    failure();
                }

                let city;
                if(responseJson.regeocode.addressComponent.city != '') {
                    city = responseJson.regeocode.addressComponent.city;
                } else {
                    city = responseJson.regeocode.addressComponent.province;
                }
                console.log({citycode: responseJson.regeocode.addressComponent.citycode, city});
                success({citycode: responseJson.regeocode.addressComponent.citycode, city});
            })
            .catch((error) =>{
                console.error(error);
                failure(error);
            });
    }

}

export default new Locator();
