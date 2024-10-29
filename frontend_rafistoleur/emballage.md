# Application d'emballage pour Android
## Introduction
​

Flet CLI fournit flet build apket flet build aabcommandes qui permettent d'emballer l'application Flet dans Android APK et Android App Bundle (AAB) respectivement.
Conditions préalables
​
Emballages de Python natifs

Les paquets Python natifs (vs "pur" paquets Python écrits en Python uniquement) sont des paquets qui sont partiellement écrits en C, Rust ou d'autres langues produisant du code natif. Exemples de colis sont numpy, cryptography, lxml, pydantic.

Lors de l'emballage de l'application Flet pour Android avec flet buildcommande de tels paquets ne peuvent pas être installés à partir du PyPI, car il n'y a pas de roues (.whl) pour la plate-forme Android.

Par conséquent, vous devez compiler des paquets natifs pour Android sur votre ordinateur avant d'exécuter flet buildcommandement.
Travaux en cours

Nous travaillons activement à l'automatisation du processus décrit ci-dessous - c'est le numéro à 1 dollar dans notre arriéré.

Flet utilise Kivy pour Android pour construire des paquets Python et Python natifs pour Android.

Pour construire votre propre distribution Python avec des paquets natifs personnalisés et l'utiliser avec flet buildcommander que vous devez utiliser p4aoutil fourni par Kivy pour Android.

p4al'outil de ligne de commande peut être exécuté sur macOS et Linux (WSL sous Windows).

Pour obtenir Android SDK d'installer Android Studio.

Sur macOS Android SDK sera situé à l'adresse suivante: $HOME/Library/Android/sdk.

Installer Temurin8 pour obtenir le JRE 1.8 requis par sdkmanageroutil:

```
brew install --cask temurin8
export JAVA_HOME=/Library/Java/JavaVirtualMachines/temurin-8.jdk/Contents/Home
````

## Fixer les variables d'environnement suivantes:

```
export ANDROID_SDK_ROOT="$HOME/Library/Android/sdk"
export NDK_VERSION=25.2.9519653##
export SDK_VERSION=android-33
````

## Ajouter un chemin à sdkmanagerà PATH:
```
export PATH=$ANDROID_SDK_ROOT/tools/bin:$PATH
````


## Installer Android SDK et NDK à partir de https://developer.android.com/ndk/downloads/ ou avec Android SDK Manager:

```
echo "y" | sdkmanager --install "ndk;$NDK_VERSION" --channel=3
echo "y" | sdkmanager --install "platforms;$SDK_VERSION"
```

## Créer un nouvel environnement virtuel Python:

```
python3 -m venv .venv
source .venv/bin/activate
```

## Install p4aà partir de la fourche de Flet - elle a épinglé Python 3.11.6 qui est compatible avec le reste du code produit par flet build:

```
pip3 install git+https://github.com/flet-dev/python-for-android.git@3.11.6
````

### Install cython:
```
pip install --upgrade cython
````

## Courir p4aavec --requirementsy compris vos bibliothèques Python personnalisées séparées avec des virgules, comme numpydans l'exemple suivant:

```
p4a create --requirements numpy --arch arm64-v8a --arch armeabi-v7a --arch x86_64 --sdk-dir $ANDROID_SDK_ROOT --ndk-dir $ANDROID_SDK_ROOT/ndk/$NDK_VERSION --dist-name mydist
````

- Choisissez Non à "Voulez-vous installer automatiquement la condition préalable JDK? [y/N.

- NOTE: La bibliothèque que vous voulez construire avec p4ala commande devrait avoir une recette dans ce dossier. Vous pouvez soumettre une demande pour faire une recette pour la bibliothèque dont vous avez besoin ou créer votre propre recette et soumettre un RP.

- Quand p4aUne commande complète un distributif Python avec vos bibliothèques personnalisées sera localisée à l'adresse suivante:

```
$HOME/.python-for-android/dists/mydist
````


### Dans le terminal où vous courez flet build apkcommander pour construire votre application Android Flet exécuter la commande suivante pour stocker le chemin distributif dans SERIOUS_PYTHON_P4A_DISTvariable de l'environnement:

```
export SERIOUS_PYTHON_P4A_DIST=$HOME/.python-for-android/dists/mydist
```

## Construisez votre application en fonctionnant flet build apkCommande à construire .apk.

- Le lot d'applications inclut maintenant des bibliothèques Python personnalisées.
flet build apk

- Construisez un fichier APK Android à partir de votre application.

- Cette commande construit la version de sortie. Les builds de 'release' ne prennent pas en charge le débogage et sont adaptés au déploiement dans les magasins d'applications. Si vous déployez l'application sur le Play Store, il est recommandé d'utiliser les Android App Bundles (AAB) ou de diviser l'APK pour réduire la taille d'APK.
```
    https://developer.android.com/guide/app-bundle
    https://developer.android.com/studio/build/configure-apk-splits-configuration-abi-split
````

Écran d'éclabou
​

Par défaut, l'application Android générée affichera un écran d'éclaboussure avec une image à partir de assetsannuaire (voir ci-dessous) ou logo Flet. Vous pouvez désactiver l'écran d'éclaboussure pour l'application Android avec --no-android-splashoption.
Installation d'APK sur un dispositif
​

Le moyen le plus simple d'installer APK sur votre appareil est d'utiliser adb(Android Debug Bridge) outil.

adbest une partie d'Android SDK. Par exemple, sur macOS, si Android SDK était installé avec Android Studio l'emplacement de adbl'outil sera à ~/Library/Android/sdk/platform-tools/adb.

Vérifiez cet article pour plus d'informations sur l'installation et l'utilisation adboutil sur différentes plateformes.

Pour installer APK sur un dispositif, exécuter la commande suivante:

adb install <path-to-your.apk>

Si plus d'un appareil est connecté à votre ordinateur (par exemple, émulateur et téléphone physique), vous pouvez utilisation -soption pour spécifier l'appareil que vous souhaitez installer .apksur:

adb -s <device> install <path-to-your.apk>

lorsque <device>peuvent être trouvés avec adb devicescommandement.
Bâtiment de la plate-forme APK
​

Par défaut, Flet construit "fat" APK qui inclut des binaires pour les deux arm64-v8aet armeabi-v7aarchitectures.

Si vous savez/contrôlez l'appareil Android, votre application sera distribuée sur vous, vous pouvez construire un APK plus petit pour une architecture spécifique.

Pour construire des APK pour arm64-v8a:

flet build apk --flutter-build-args=--target-platform --flutter-build-args=android-arm64

Pour construire des APK pour armeabi-v7a:

flet build apk --flutter-build-args=--target-platform --flutter-build-args=android-arm

Dépannage d'Android
​

Pour exécuter des commandes interactives à l'intérieur du simulateur ou du dispositif:

adb shell

Pour surmonter l'erreur "permissions refusées" tout en essayant de parcourir le système de fichiers dans le shell Android interactif:

su

Pour télécharger un fichier d'un appareil sur votre ordinateur local:

adb pull <device-path> <local-path>

flet build aab

Construisez un fichier Android App Bundle (AAB) à partir de votre application.

Cette commande construit la version de sortie. Les builds de 'release' ne prennent pas en charge le débogage et sont adaptés au déploiement dans les magasins d'applications. L'App bundle est la façon recommandée de publier sur le Play Store car il améliore la taille de votre application.
Écran d'éclabou
​

Par défaut, l'application Android générée affichera un écran d'éclaboussure avec une image à partir de assetsannuaire (voir ci-dessous) ou logo Flet. Vous pouvez désactiver l'écran d'éclaboussure pour l'application Android avec --no-android-splashoption.