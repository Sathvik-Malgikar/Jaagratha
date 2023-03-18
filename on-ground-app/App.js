import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View,Image ,ImageBackground , Platform} from 'react-native';
import { useState } from 'react';
// const Sound =  require("react-native-sound");
// import * as Device from 'expo-device';
// import * as Notifications from 'expo-notifications';

// Notifications.setNotificationHandler({
//   handleNotification: async () =>{ 

//     return({
//     shouldShowAlert: true,
//     shouldPlaySound: true,
//     shouldSetBadge: false,
//   })}
// });


// async function registerForPushNotificationsAsync() {
//   let token;
//   if (Device.isDevice) {
//     const { status: existingStatus } = await Notifications.getPermissionsAsync();
//     let finalStatus = existingStatus;
//     if (existingStatus !== 'granted') {
//       const { status } = await Notifications.requestPermissionsAsync();
//       finalStatus = status;
//     }
//     if (finalStatus !== 'granted') {
//       alert('Failed to get push token for push notification!');
//       return;
//     }
//     token = (await Notifications.getExpoPushTokenAsync()).data;
//     console.log(token);
//   } else {
//     alert('Must use physical device for Push Notifications');
//   }

//   if (Platform.OS === 'android') {
//     Notifications.setNotificationChannelAsync('default', {
//       name: 'default',
//       importance: Notifications.AndroidImportance.MAX,
//       vibrationPattern: [0, 250, 250, 250],
//       lightColor: '#FF231F7C',
//     });
//   }

//   return token;
// }

export default function App() {
  // const [expoPushToken, setExpoPushToken] = useState('');
  // const [notification, setNotification] = useState(false);
  // const notificationListener = useRef();
  // const responseListener = useRef();


  // useEffect(() => {
  //   registerForPushNotificationsAsync().then(token => setExpoPushToken(token));

  //   notificationListener.current = Notifications.addNotificationReceivedListener(notification => {
  //     setNotification(notification);
  //   });

  //   responseListener.current = Notifications.addNotificationResponseReceivedListener(response => {
  //     console.log(response);
  //   });

  //   return () => {
  //     Notifications.removeNotificationSubscription(notificationListener.current);
  //     Notifications.removeNotificationSubscription(responseListener.current);
  //   };
  // }, []);

  // async function sendPushNotification(expoPushToken) {
  //   const message = {
  //     to: expoPushToken,
  //     sound: 'default',
  //     title: 'Alert from HeadQuarters.!',
  //     body: 'A medium level alert has been raised in Basavangudi area',
  //     data: { someData: 'goes here' },
  //   };
  // }

//   function handleSoundPlay() {
    
//     let alert = new Sound('alert.mp3', Sound.MAIN_BUNDLE, (error) => {
//         if (error) {
//           console.log(error)
//         }
//       })

//       alert.play((success) => {
//         if (!success) {
//           console.log('Sound did not play :(')
//         }
//       })
// }
// handleSoundPlay()

  const [alertset, setalertset] = useState(false)

  let user = {"name" :"Ramkumar bhadoria" , "area" : "Basavangudi"}



const bg = {"uri" : "https://reactjs.org/logo-og.png"};
  return (
    <View style={styles.container}>
    {/* <ImageBackground style={styles.image} resizeMode='cover' source={require("./assets/bg3.jpg")}> */}

   <View style={styles.nameplate} >

   <Text style={styles.nametext}>Name : {user.name}</Text>
   <Text style={styles.nametext}> Area serving currently : {user.area}</Text>
   </View>

   { alertset?<>
   
   </> : <Text style={styles.nametextw}>No messages from the Headquarters yet..</Text>}

    <Image source={require("https://www.clipartmax.com/png/middle/470-4704082_glossy-sos-circle-button-clip-art-sos-button-clip-art.png")}></Image>

    {/* </ImageBackground> */}
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  image: {
    flex: 1,
    
    justifyContent: 'center',
  },
  container: {
    flex: 1,
    

    alignItems: 'center',
    justifyContent: 'space-around',
  },
  nameplate: {
    

    width : 200,
    left : 80,
    padding : 10,
    margin : 30,
    
    // flex: 1,
    backgroundColor: '#9999ff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  nametext :{
    fontSize : 20,
  },
  nametextw :{
    fontSize : 20,
    color : "white"
  }
});

