# **3) endpoint_performance_insights/README.md**

```markdown
#  Endpoint Performance Insights (Endpoint Central Style)

Synthetic dataset of **2,500 endpoints** replicating device health data from tools like ManageEngine Endpoint Central.

---

##  Analyzed Fields
- CPU %  
- Memory %  
- Patch Compliance  
- Deployment Success  
- Last Seen Timestamp  

---

##  Files
- `endpoints.csv`
- `analysis_endpoints.py`
- `cpu_distribution.png`
- `LICENSE.txt`

---

##  Generated Chart
CPU usage distribution:

![CPU Chart](cpu_distribution.png)

---

##  Run Script
```bash
python analysis_endpoints.py
