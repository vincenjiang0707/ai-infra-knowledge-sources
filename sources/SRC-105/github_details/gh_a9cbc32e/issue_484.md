# [Issue #484] How to pre-populate datasource settings via env. variables?

source: https://github.com/ROCm/rocprofiler-compute/issues/484
state: closed | updated: 2024-12-06T16:12:23Z
labels: question, Under Investigation

## 正文

### Describe your question

Happy Friday! 
I would like to populate omniperf datasource settings automagically.  I am injecting the values of the MongoDB URL via env. variables into the Grafana container. 
is there any way that when I try to add Omniperf as a datasource I can prepopulate this page:
https://rocm.docs.amd.com/projects/omniperf/en/latest/_images/datasource_settings.jpg
Thanks!
ElCap 1

### Additional context

![image](https://github.com/user-attachments/assets/54af33ff-ad4c-40cd-b0d6-b6fcc97b1db9)


## 评论 (2)

### tcgu-amd · 2024-11-25

Hi @ELCapitanLLNL, thanks for reaching out! Unfortunately, there is no straightforward method to achieve what you are describing at the moment. However, there is a "hackish" way that might get it to work through using a custom entrypoint file that modifies the html and json source code for the rocprofiler-compute plugin. 

For example, you can create a entrypoint file "foo.sh" that looks like this
```
#!/bin/bash
CONFIG_HTML=/var/lib/grafana/plugins/rocprofiler-compute_plugin/src/html/config.html
DEFAULT_JSON=/var/lib/grafana/plugins/rocprofiler-compute_plugin/server/config/default.json
#DEFAULT_JSON=/var/lib/grafana/plugins/omniperf_plugin/server/config/default.json
#CONFIG_HTML=/var/lib/grafana/plugins/omniperf_plugin/src/html/config.html
sed -i -e 's|mongodb://localhost:27017|'"$MONGO_URL"'|g' -e 's|myDatabase|'"$MONGO_NAME"'|g' -e 's|placeholder|value|g' $CONFIG_HTML
sed -i -e 's|3333|'"$MY_PORT"'|g' $DEFAULT_JSON
/docker-entrypoint.sh
```
(We recently changed the path names to `rocprofiler-compute_plugin`. Switch to the commented out variables on the top if yours still say `omniperf_plugin`.)

The script above assumes that your MongoDB url and name are stored in `MONGO_URL` and `MONGO_NAME` respectively, and the http port is in `MY_PORT`.

Then, you can modify the `web` service in the `docker-compose.yml` as

```
  web:
    image: rocprofiler-compute-grafana-v1.0
    container_name: rocprofiler-compute-grafana-v1.0
    restart: always
    build: .
    environment:
      - GF_PATHS_CONFIG="grafana/etc/grafana.ini"
      - GF_PLUGINS_ALLOW_LOADING_UNSIGNED_PLUGINS=amd-rocprofiler-compute-data-plugin
      - GF_DEFAULT_APP_MODE=development
      - MONGO_URL=foo
      - MONGO_NAME=bar
      - MY_PORT=12345
    ports:
      - "14000:4000"
    volumes:
      - grafana-storage:/var/lib/grafana
      - ./foo.sh:/app/foo.sh
    stdin_open: true
    tty: true
    entrypoint: ["/app/foo.sh"]
```
Please keep in mind that due to the hacky nature of this solution, it might not be very stable. More robust `sed` commands might also be a good idea. Please feel free to reach out if you have any questions! 

Thanks!


### tcgu-amd · 2024-12-06

Hi, this issue will be closed for now due to inactivity. Please feel free to reopen for updates and follow ups. Thanks!
