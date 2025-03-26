## Low-Level Design (LLD)

Below is the Low-Level Design (LLD) for the backend API and its integration with the ML pipelines:

### LLD Diagram
![Low-Level Design](./docs/images/LLD_diagram.png)

---

### Description of Components in the LLD

1. **Controller Layer**  
   - **Responsibilities**:  
     - Handles incoming API requests.  
     - Validates the payload (e.g., checking schema or ensuring all required fields are present).  
     - Forwards requests to the Service Layer.

2. **Service Layer**  
   - **Responsibilities**:  
     - Processes the incoming data from the controller layer.  
     - Converts raw input into a format compatible with the ML models.  
     - Handles business logic, including fetching metadata or configurations.  
     - Sends formatted requests to the ML Model Handler.

3. **Model Handler**  
   - **Responsibilities**:  
     - Interacts with pre-trained ML models (stored in `/models`).  
     - Ensures that model input/output dimensions and formats match the prediction pipeline.  
     - Implements model failovers (if necessary).

4. **Database/Cache Layer**  
   - **Responsibilities**:  
     - Stores metadata about predictions, logs, or configurations.  
     - Enables caching for frequently requested predictions to optimize response time.  
     - Handles secure storage of sensitive data.

---

### API Request-Response Flow

1. **API Endpoint**:  
   - `POST /api/v1/predict`  
     - **Input**: JSON payload with model input data.  
     - **Output**: Prediction results in JSON format.

2. **Request Flow**:  
   - Client → Controller → Service Layer → ML Model Handler → Response.

3. **Error Handling**:  
   - If validation fails, the controller returns a `400 Bad Request`.  
   - If the model fails to respond, a `503 Service Unavailable` is returned.  
   - If processing errors occur in the service layer, a `500 Internal Server Error` is returned.

---

### Note: 
The actual LLD diagram file can be found in `docs/images/LLD_diagram.png`. Make sure to update the path if you relocate the image in the folder structure.
