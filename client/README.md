## Get started

1. Install dependencies

   ```bash
   npm install
   ```

2.1. Prebuild App

   ```bash
   npx expo prebuild                         // android+ios build
   npx expo prebuild --platform ios          // ios build
   npx expo prebuild --platform android      // android build
   ```

2.2 Build and Run App

   ```bash
   npx expo run:ios          // ios build
   npx expo run:android      // android build
   ```

In the output, you'll find options to open the app in a

- [development build](https://docs.expo.dev/develop/development-builds/introduction/)
- [Android emulator](https://docs.expo.dev/workflow/android-studio-emulator/)
- [iOS simulator](https://docs.expo.dev/workflow/ios-simulator/)
- [Expo Go](https://expo.dev/go), a limited sandbox for trying out app development with Expo
