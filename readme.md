# Information about the project

Python 3.8.10 was the python version used in this project.  
Use the requirements.txt file for the other dependencies needed.  
Load the dependencies in a python environment with:  
```
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```
Running the commands above after installing python 3.8.10 should assure everything runs smoothly.

# About running this project
After installing the right version of python and the requirements from `requirements.txt` as stated above,
activate the virtual environment with `source env/bin/activate`,
then you can run the build_doc_bins.py with `python src/build_doc_bins.py`.  
After running the above command, the spacy `doc_bins` will have been generated, then you can run the training command to train the model with the `doc_bins`: `python -m spacy train ./config.cfg`  
The trained model will be stored in the `target` folder.
After this you can run `python src/using_trained_model.py` to see the result given by the trained model.

# How the training configuration file was generated
```
python -m spacy init config ./config.cfg --lang en --pipeline ner
```
## Explaining the command:
The command `python -m spacy init config` takes one argument, the path to where the config file will be generated.  
Here, 2 flags were used as well, the `--lang`, to specify the configuration file language, and the `--pipeline` to specify which allows you to specify a comma separated list of pipeline components that will be targeted for the training. In this case, there is only one being specified, which is the NamedEntityRecofnition component.  

# Training a pipeline
To train a pipeline, run the following
```
python -m spacy train ./config.cfg --output ./target --paths.train doc_bins/train.doc_bin.spacy --paths.dev dev.doc_bin.spacy
```
The `--output` flag specify the place where the trained model will be saved.  
The `--paths.train` flag specify the training data file. 
The `--paths.dev` flag specify the test data file. 

# Loading and using the trained pipeline.
The output of the training will be a regular loadable Spacy pipeline.  
`model-last`: is the last trained pipeline.  
`model-best`: The best trained pipeline.  

```
import spacy

nlp = spacy.load("/path/to/output/model-best")
doc = nlp("iPhone 11 vs iPhone 8: What's the difference?")
print(doc.ents)
```

# Interpreting the output of the trained model:

[Meaning of NER Training Values](https://datascience.stackexchange.com/questions/103062/meaning-of-ner-training-values-using-spacy)  

Example of the output after training a model:
  
<img src="project_images/training.png"  width="460" height="500">

---
# Phrase production plan.
Getting more information from the Making Things Talk Book, it follows that devices can be split into three categories,  
`Sensors`, `Actuators` and `Tags`.
Asking chat GPT to produce examples of each of these entities, we had an interaction as follows:

## Sensor Examples
```
sensors are an type of IoT devices.

Give me an exhaustive list of IoT sensors?

As an AI language model, I can provide a list of commonly used IoT sensors, but it may not be exhaustive, as new types of sensors are being developed regularly. Here are some examples of IoT sensors:

Temperature sensors
Humidity sensors
Pressure sensors
Light sensors
Proximity sensors
Motion sensors
Accelerometers
Gyroscopes
Magnetometers
Gas sensors
Sound sensors
Image sensors
Water quality sensors
pH sensors
Radiation sensors
Biometric sensors
Proximity sensors
Occupancy sensors
Vibration sensors
Flow sensors
Soil moisture sensors
CO2 sensors
Smoke sensors
GPS sensors
Infrared sensors
Ultrasonic sensors
Optical sensors
Inertial measurement units (IMUs)
Strain sensors
Load cells.
Please note that this is not an exhaustive list, and there are many other types of sensors used in IoT applications. The choice of sensor depends on the application and the data required.

```

## Tag Examples
```
Tags are an type of IoT devices.

Give me an exhaustive list of IoT tags?
Tags can be used in IoT applications for various purposes such as tracking, inventory management, asset management, and more. Here are some examples of IoT tags:

RFID (Radio Frequency Identification) tags
NFC (Near Field Communication) tags
Bluetooth Low Energy (BLE) tags
GPS (Global Positioning System) tags
QR (Quick Response) code tags
Barcodes tags
Magnetic tags
Active RFID tags
Passive RFID tags
Electronic article surveillance (EAS) tags
Wi-Fi tags
Zigbee tags
LoRa tags
UWB (Ultra-Wideband) tags
Smart labels
Sensor tags
It's important to note that there are many different types of IoT tags, and their applications and specifications may vary depending on the use case. Some tags may be suitable for tracking large objects or vehicles, while others may be designed for tracking smaller items or people. The choice of tag depends on the specific requirements of the application.




Cristóvão Iglesias
Give me more examples of IoT tags?
Sure, here are some additional examples of IoT tags:

Passive UHF RFID tags
Active UHF RFID tags
Zigbee asset tags
Wi-Fi asset tags
Asset labels with tamper-evident features
Sensor-equipped asset tags for monitoring temperature, humidity, vibration, and more
Bluetooth asset tags with replaceable batteries
GPS tracking tags for vehicles and equipment
NFC-enabled asset tags for mobile payments, loyalty programs, and access control
Long-range UHF RFID tags for inventory management in warehouses and distribution centers
RTLS (Real-Time Location System) tags for tracking the location of people, equipment, and assets indoors
Barcode asset tags with embedded RFID technology for hybrid tracking solutions
RAIN RFID tags for tracking and managing goods in retail and supply chain environments
NFC-enabled smart tags for personalized customer experiences in retail, hospitality, and entertainment
Disposable RFID tags for one-time use in event management and access control.
Again, it's important to note that there are many different types of IoT tags available, and the choice of tag depends on the specific requirements of the application.

```

## Actuator examples
```
Actuators are an Special IoT Device that executes a change in the physical state
of one or more Physical Entities.

Actuators can modify the physical state of a Physical Entity, like changing the
state (translate, rotate, stir, inflate, switch on/off,. . .) of simple Physical Entities
or activating/deactivating functionalities of more complex ones

Give me an exhaustive list of IoT Actuators?



As an AI language model, I can provide a list of commonly used IoT actuators, but it may not be exhaustive, as new types of actuators are being developed regularly. Here are some examples of IoT actuators:

Motors
Servo motors
Linear actuators
Solenoids
Valves
Relays
LED lights
Heating elements
Cooling fans
Pumps
Electromagnets
Speakers
Display screens
Switches
Locks
Door openers
Curtains/blinds controllers
Robotic arms
Drones
3D printers
Please note that this is not an exhaustive list, and there are many other types of actuators used in IoT applications. The choice of actuator depends on the application and the action required.

```

## Definitions

```
🚨Device:
Technical physical component (hardware) with communication capabilities to other ITC systems. A device can
be either attached to or embedded inside a Physical
Entity, or monitor a Physical Entity in its vicinity
Devices: the sensors/actuators needed and where are they situated; their
relationship to the Physical Entity (directly mounted; touching; remote but in
sight . . .), etc. Note that the device choice is influenced by the Physical Entity. In
the recurring example, it is too expensive (in relation to the market price of the
Physical Entity) to measure the temperature of each orchid. Instead, sensors that
measure the air temperature are situated inside the cargo area. It is then assumed
that the air temperature equals that of the orchids. In other words, the Physical
Entity model also needs to include a sensing and/or an actuating model.

🚨Tag:
Label or other physical object used to identify the Physical
Entity to which it is attached.
are used to identify Physical Entities, to which the Tags are usually
physically attached. The identification process is called “reading”, and it is
carried out by specific Sensor Devices, which are usually called readers. The
primary purpose of Tags is to facilitate and increase the accuracy of the
identification process. This process can be optical, as in the case of barcodes
and QR codes, or it can be RF-based, as in the case of microwave car-plate
recognition systems and RFID. The actual physics of the process, as well as the
many types of tags, are however irrelevant for the IoT Domain Model as these
technologies vary and change over time. These are important however when
selecting the right technology for the implementation of a concrete system;

🚨Actuator:
Special Device that executes a change in the physical state
of one or more Physical Entities
Actuators can modify the physical state of a Physical Entity, like changing the
state (translate, rotate, stir, inflate, switch on/off,. . .) of simple Physical Entities
or activating/deactivating functionalities of more complex ones.

🚨 Sensors:
provide information, knowledge, or data about the Physical Entity they
monitor. In this context, this ranges from the identity of the Physical Entity to
measures of the physical state of the Physical Entity. Like other Devices, they
can be attached or otherwise embedded in the physical structure of the Physical
Entity, or be placed in the environment and indirectly monitor Physical Entities.
An example for the latter is a face-recognition enabled camera. Information from
sensors can be recorded for later retrieval (e.g., in a storage of Resource);
Special Device that measures physical characteristics of
one or more Physical Entities.

```