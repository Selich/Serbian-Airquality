export const getAQI = async () => {
  const url = 'https://flask-app-airquality.herokuapp.com/'
  try{
    const res = await fetch(url)
    return await res.json()
  } catch (e){
    console.log(e);
  }
}