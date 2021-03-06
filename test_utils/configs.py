
testDeploymentConfig = {
    "name": "foo-service",
    "description": "This is a sample service generated by kubedev.",
    "imagePullSecrets": "foo-creds",
    "imageRegistry": "foo-registry",
    "required-envs": {
        "FOO_SERVICE_GLOBAL_ENV1": {
            "documentation": "Test env var #1 (global)"
        },
        "FOO_SERVICE_GLOBAL_ENV2": {
            "documentation": "Test env var #1 (global)",
            "build": True,
            "container": False
        },
    },
    "deployments": {
        "foo-deploy": {
            "ports": {
                "http": {
                    "container": "8081",
                    "service": "8082",
                    "dev": "8083"
                },
                "https": {
                    "container": "8443",
                    "service": "8543",
                    "dev": "8643"
                },
            },
            "volumes": {
              "dev": {
                "output_docker": "/test/output"
              }
            },
            "required-envs": {
                "FOO_SERVICE_DEPLOY_ENV1": {
                    "documentation": "Test env var #1"
                },
                "FOO_SERVICE_DEPLOY_ENV2": {
                    "documentation": "Test env var #2",
                    "container": True
                },
                "FOO_SERVICE_DEPLOY_ENV3": {
                    "build": True,
                    "container": False
                }
            }
        }
    }
}

testMultiDeploymentsConfig = {
    "name": "foo-service",
    "description": "This is a sample service generated by kubedev.",
    "imagePullSecrets": "foo-creds",
    "imageRegistry": "foo-registry",
    "required-envs": {
        "FOO_SERVICE_GLOBAL_ENV1": {
            "documentation": "Test env var #1 (global)",
            "build": False
        },
        "FOO_SERVICE_GLOBAL_ENV2": {
            "documentation": "Test env var #2 (global)"
        },
    },
    "deployments": {
        "foo-deploy": {
            "ports": {
                "http": {
                    "container": "8081",
                    "service": "8082",
                    "dev": "8083"
                },
                "https": {
                    "container": "8443",
                    "service": "8543",
                    "dev": "8643"
                },
            },
            "required-envs": {
                "FOO_SERVICE_DEPLOY_ENV1": {
                    "documentation": "Test env var #1, service 'foo-deploy'"
                },
                "FOO_SERVICE_DEPLOY_ENV2": {
                    "documentation": "Test env var #2, service 'foo-deploy'",
                    "build": False
                }
            }
        },
        "bar-deploy": {
            "ports": {
                "http": {
                    "container": "3081",
                    "service": "3082",
                    "dev": "3083"
                },
                "https": {
                    "container": "3443",
                    "service": "3543",
                    "dev": "3643"
                },
            },
            "required-envs": {
                "BAR_SERVICE_DEPLOY_ENV1": {
                    "documentation": "Test env var #1, service 'bar-deploy'",
                    "build": False
                },
                "BAR_SERVICE_DEPLOY_ENV2": {
                    "documentation": "Test env var #2, service 'bar-deploy'"
                }
            }
        }
    }
}

testMixedSubProjectsConfig = {
    "name": "foo-service",
    "description": "This is a sample service generated by kubedev.",
    "imagePullSecrets": "foo-creds",
    "imageRegistry": "foo-registry",
    "required-envs": {
        "FOO_SERVICE_GLOBAL_ENV1": {
            "documentation": "Test env var #1 (global)",
            "build": False
        },
        "FOO_SERVICE_GLOBAL_ENV2": {
            "documentation": "Test env var #2 (global)"
        },
    },
    "deployments": {
        "foo-deploy": {
            "ports": {
                "http": {
                    "container": "8081",
                    "service": "8082",
                    "dev": "8083"
                },
                "https": {
                    "container": "8443",
                    "service": "8543",
                    "dev": "8643"
                },
            },
            "required-envs": {
                "FOO_SERVICE_DEPLOY_ENV1": {
                    "documentation": "Test env var #1, service 'foo-deploy'"
                },
                "FOO_SERVICE_DEPLOY_ENV2": {
                    "documentation": "Test env var #2, service 'foo-deploy'",
                    "build": False
                }
            }
        },
        "bar-deploy": {
            "ports": {
                "http": {
                    "container": "3081",
                    "service": "3082",
                    "dev": "3083"
                },
                "https": {
                    "container": "3443",
                    "service": "3543",
                    "dev": "3643"
                },
            },
            "required-envs": {
                "BAR_SERVICE_DEPLOY_ENV1": {
                    "documentation": "Test env var #1, service 'bar-deploy'",
                    "build": False
                },
                "BAR_SERVICE_DEPLOY_ENV2": {
                    "documentation": "Test env var #2, service 'bar-deploy'"
                }
            }
        }
    },
    "cronjobs": {
      # TODO
    }
}
