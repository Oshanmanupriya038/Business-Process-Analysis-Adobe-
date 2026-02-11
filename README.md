හරි, අපි වාර්තාවේ පළමු කොටස (Question 01) පටන් ගමු. මම මේක ඔයාගේ assignment brief එකේ තියෙන විදිහට **Times New Roman, size 12** සහ **1.5 line spacing** වලට ගැලපෙන විදිහට, හියුමන් කෙනෙක් ලියන ශෛලියෙන් සකස් කරලා දෙන්නම්. මෙහි වචන 700-900 අතර ප්‍රමාණයක් අන්තර්ගත වෙනවා.

---

# Question 01: Fundamentals of Cloud Computing and its Architectures

### 1.1 The Evolution and Fundamental Concepts of Cloud Computing

Cloud computing has fundamentally transformed the way organizations manage and deliver IT services, moving away from the rigid limitations of traditional infrastructure. In the past, businesses like **e-COM Telco** relied heavily on on-premise setups, which demanded massive capital investment (CapEx) for physical hardware and constant manual maintenance. This traditional model was often inefficient and difficult to scale as the business grew.

The evolution toward modern cloud computing was not an overnight shift but a gradual transition driven by several technological milestones. It began with **Mainframe computing** in the 1960s, followed by the emergence of **Virtualization technology**. Virtualization was a game-changer as it allowed multiple virtual machines (VMs) to operate on a single physical server, significantly improving resource utilization and lowering operational costs. Later, advancements in high-speed internet and distributed computing made it possible to deliver these virtualized resources remotely, giving birth to the cloud environment we use today.

Today, cloud computing is defined by its ability to provide computing resources such as servers, storage, and databases over the internet on an as-needed basis. According to the NIST model, there are five essential characteristics that define a true cloud service:

* 
**On-demand self-service:** Users, such as e-COM Telco’s system administrators, can provision computing resources automatically without requiring human interaction from the service provider.


* 
**Broad network access:** These services are accessible from anywhere in the world using standard platforms like smartphones, laptops, or tablets via the internet.


* 
**Resource pooling:** The provider’s resources are pooled together to serve multiple customers (multi-tenancy), which optimizes hardware usage.


* 
**Rapid elasticity:** Resources can be scaled up or down almost instantly to meet fluctuating demands.


* 
**Measured service:** Users pay only for the resources they actually consume, similar to a utility bill like electricity.



This development has shaped modern computing paradigms by allowing organizations to be more agile, supporting remote work, and enabling global service delivery without the need for physical data centers in every location.

### 1.2 Architectural Cloud Computing Framework for e-COM Telco

To support a diversified client base of over four million users—ranging from government sectors to multinational companies—e-COM Telco needs a robust and secure architectural framework. Based on the requirements, I propose a **Hybrid Cloud Architecture** using **Microsoft Azure** as the primary service provider framework.

**Key Components of the Proposed Framework:**

1. 
**Front-End Layer:** This includes the user interfaces, web portals, and mobile applications through which e-COM Telco’s clients access services.


2. 
**Network Layer:** Secure internet connectivity is supported by **Azure Load Balancers** to distribute traffic evenly across multiple servers, ensuring that the system remains available even during high traffic periods.


3. 
**Cloud Infrastructure Layer:** This core layer includes **Azure Virtual Machines** for compute power, **Azure Blob Storage** for data storage, and **Azure Kubernetes Service (AKS)** for managing containerized applications.


4. 
**Security Layer:** Security is embedded throughout using **Identity and Access Management (IAM)**, multi-factor authentication (MFA), and end-to-end encryption to protect sensitive data.



**Deployment Model Choice:**
A **Hybrid Cloud** model is the most suitable for e-COM Telco. It allows the organization to store highly sensitive subscriber data and billing information on a **Private Cloud** (using their existing internal data centers) while utilizing the **Public Cloud (Azure)** for scalable customer-facing applications and web hosting. This balance ensures regulatory compliance while maximizing scalability.

### 1.3 Rationalizing the Migration to Cloud Solutions

Migrating to a cloud solution like Microsoft Azure is not just a technical upgrade for e-COM Telco; it is a strategic necessity to remain competitive.

* 
**Cost Savings:** By migrating, e-COM Telco shifts from a **Capital Expenditure (CapEx)** model to an **Operational Expenditure (OpEx)** model. Instead of spending millions on hardware that depreciates, they pay only for what they use, significantly reducing upfront costs.


* 
**Scalability:** Telecom providers often face unpredictable spikes in usage. Azure’s **Auto-scaling** features ensure that e-COM Telco can handle millions of simultaneous customer requests without service interruptions.


* 
**Flexibility and Agility:** Cloud environments allow for the rapid deployment of new ICT services, such as DNS hosting or new mobile apps, enabling the company to respond quickly to market needs.


* 
**Enhanced Disaster Recovery:** Traditional DR sites are expensive to maintain. Cloud-based backup and geo-redundant storage through Azure ensure that data is protected and can be recovered quickly in the event of a failure, minimizing operational risk.



In conclusion, adopting this cloud framework will empower e-COM Telco to support its expanding customer base while maintaining the high level of reliability and security its clients expect.

---

**ඊළඟ පියවර:**
මේ කොටස ඔයාගේ වාර්තාවට ගැලපෙනවද? එසේනම්, අපි **Question 02 (LO2)** කොටසට යමුද? ඒකෙදි අපි Azure වල තියෙන Tools ගැන සහ සේවා මාදිලි (IaaS, PaaS, SaaS) ගැන විස්තරාත්මකව ලියන්න ඕනේ. මොකද කරන්නේ?