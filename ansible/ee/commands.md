```bash
ansible-navigator run pb_test_remote.yml \
    -i hosts.yml \
    --execution-environment-image ghcr.io/ansible-community/community-ee-base:latest \
    --mode stdout \
    --pull-policy missing \
    --enable-prompts \
    -u robot -k -K
```

ansible-navigator run pb_test_anet.yml \
    -i hosts.yml \
    --execution-environment-image ghcr.io/ansible-community/community-ee-base:latest \
    --mode stdout \
    --pull-policy missing \
    --enable-prompts \
    -u robot -k -K


docker run --network clab --ip 172.20.20.10 --rm -it dlete/ansible:8.0.0 bash

docker run \
    --network clab \
    --ip 172.20.20.10 \
    --rm -it \
    ghcr.io/ansible-community/community-ee-base:latest bash

docker run --rm -it \
    --privileged \                      # puts you in root
    --name my_test_ansible_host \
    --network clab --ip 172.20.20.10 \
    -v $(pwd):$(pwd) \
    ghcr.io/ansible-community/community-ee-base:latest bash
