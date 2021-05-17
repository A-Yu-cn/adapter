import requests

post_data = {
    "object_kind": "push",
    "event_name": "push",
    "before": "0101010101010101010101010101010101010101",
    "after": "0123456789012345678901234567890123456789",
    "ref": "refs/heads/master",
    "checkout_sha": "0123456789012345678901234567890123456789",
    "message": "",
    "user_id": 1234,
    "user_name": "example_user",
    "user_username": "example_user",
    "user_email": "example@huawei.com",
    "user_avatar": 'null',
    "project_id": 123456,
    "project": {
        "id": 123456,
        "name": "ExampleRepository",
        "description": "This is an example repository",
        "web_url": "https://codehub.devcloud.huaweicloud.com/ExampleNamespace/ExampleRepository",
        "avatar_url": 'null',
        "git_ssh_url": "git@codehub.devcloud.huaweicloud.com:ExampleNamespace/ExampleRepository.git",
        "git_http_url": "https://codehub.devcloud.huaweicloud.com/ExampleNamespace/ExampleRepository.git",
        "namespace": "ExampleNamespace",
        "visibility_level": 0,
        "path_with_namespace": "ExampleNamespace/ExampleRepository",
        "default_branch": "master",
        "ci_config_path": 'null',
        "homepage": "https://codehub.devcloud.huaweicloud.com/ExampleNamespace/ExampleRepository",
        "url": "git@codehub.devcloud.huaweicloud.com:ExampleNamespace/ExampleRepository.git",
        "ssh_url": "git@codehub.devcloud.huaweicloud.com:ExampleNamespace/ExampleRepository.git",
        "http_url": "https://codehub.devcloud.huaweicloud.com/ExampleNamespace/ExampleRepository.git"
    },
    "commits": {
        "id": "0123456789012345678901234567890123456789",
        "message": "This is an example message",
        "timestamp": "2019-05-30T08:50:37Z",
        "url": "https://codehub.devcloud.huaweicloud.com/ExampleNamespace/ExampleRepository/commit/0123456789012345678901234567890123456789",
        "author": {
            "name": "example_user",
            "email": "example@huawei.com"
        }, "added": [
            "src/main/java/HelloWorld.java"
        ],
        "modified": [],
        "removed": []
    },
    "total_commits_count": 1,
    "repository": {
        "name": "ExampleRepository",
        "url": "git@codehub.devcloud.huaweicloud.com:ExampleNamespace/ExampleRepository.git",
        "description": "This is an example repository",
        "homepage": "https://codehub.devcloud.huaweicloud.com/ExampleNamespace/ExampleRepository",
        "git_http_url": "https://codehub.devcloud.huaweicloud.com/ExampleNamespace/ExampleRepository.git",
        "git_ssh_url": "git@codehub.devcloud.huaweicloud.com:ExampleNamespace/ExampleRepository.git",
        "visibility_level": 0
    }
}
if __name__ == "__main__":
    res = requests.post(url="http://127.0.0.1:666//api/webhook", data=post_data)
    print(res.text)
