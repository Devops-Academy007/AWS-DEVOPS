# AWS-DEVOPS

# DevOps: Zero to Job-Ready

A hands-on, 3-month DevOps course taking a complete beginner from the Linux command line to deploying and monitoring real infrastructure on AWS. Built around the tools that hiring managers actually ask for.

This repository is the home base for the course: it holds the notes, labs, homework, and portfolio projects for all twelve weeks. Everything here is written to be followed step by step, with no prior DevOps knowledge assumed.

---

## What this course covers

The course is built in three phases, each roughly one month. Every phase builds on the one before it, so the order matters — Docker only makes sense once you know Linux, and Kubernetes only makes sense once you know Docker.

**Month 1 — Foundations.** Linux and the command line, shell scripting, Git and GitHub, and how networking and the web actually work.

**Month 2 — Core DevOps.** Docker and containers, building CI/CD pipelines with GitHub Actions, and the core AWS services used to run applications in the cloud.

**Month 3 — Scale and Job Readiness.** Kubernetes essentials, infrastructure as code with Terraform, monitoring and logging, and a final capstone project plus interview preparation.

---

## Repository structure

```
.
├── README.md              This file
├── references/            Cheat sheets and quick-reference material
│   └── linux-cheatsheet.md
├── week-01-linux/         Linux and the command line
│   ├── notes/             Teaching notes and concepts
│   ├── labs/             In-session practical exercises
│   └── homework/          Weekly assignments
├── week-02-scripting/     Shell scripting with Bash
├── week-03-git/           Git and GitHub
├── week-04-networking/    Networking and web fundamentals
├── week-05-docker/        Docker basics
├── week-06-compose/       Docker Compose and image registries
├── week-07-cicd/          CI/CD with GitHub Actions
├── week-08-aws/           AWS core services
├── week-09-kubernetes/    Kubernetes essentials
├── week-10-terraform/     Terraform and infrastructure as code
├── week-11-monitoring/    Monitoring and logging
├── week-12-capstone/      Capstone project and interview prep
└── projects/              The three portfolio projects
    ├── 01-server-toolkit/
    ├── 02-containerized-app/
    └── 03-platform-capstone/
```

Each weekly folder follows the same layout: `notes/` for concepts, `labs/` for the exercises done together during a session, and `homework/` for the assignment due before the next session.

---

## The 12-week plan

| Week | Topic | Milestone |
|---|---|---|
| 1 | Linux fundamentals | Comfortable navigating and working in a terminal |
| 2 | Shell scripting | First automation script written and version-controlled |
| 3 | Git and GitHub | Clean commits, branches, and pull requests |
| 4 | Networking and web | Understand how a request reaches a server |
| 5 | Docker basics | First application running in a container |
| 6 | Compose and registries | Multi-container app stack |
| 7 | CI/CD with GitHub Actions | Automated build-and-test pipeline |
| 8 | AWS core services | Container deployed to a real AWS server |
| 9 | Kubernetes essentials | App running on a local cluster |
| 10 | Terraform | Infrastructure defined entirely as code |
| 11 | Monitoring and logging | A monitored, observable application |
| 12 | Projects | Portfolio complete, interview-ready |

---

## Portfolio projects

Hiring managers open GitHub before they open a CV. Each month ends with a project that lands in the `projects/` folder, and by the end of the course these three pieces are the strongest evidence of skill.

**1. Server Automation Toolkit** *(end of Month 1)* — A set of Bash scripts that provision, harden, and back up a Linux server, scheduled with cron and documented on GitHub.

**2. Containerized App with CI/CD** *(end of Month 2)* — A web application packaged with Docker, built and tested by a GitHub Actions pipeline, and automatically deployed to AWS on every push.

**3. Full Platform Capstone** *(end of Month 3)* — Terraform provisions the infrastructure, Kubernetes runs the application, and Prometheus and Grafana monitor it — a miniature of a real production platform.

---

## Tools and technologies

Linux · Bash · Git and GitHub · Docker · GitHub Actions · AWS (EC2, S3, IAM, VPC) · Kubernetes · Terraform · Prometheus · Grafana

---

## How to use this repository

If you are the student taking this course:

1. Clone this repository to your machine and keep it open in your editor.
2. Before each session, skim the `notes/` folder for that week.
3. During each session, work through the `labs/` exercises hands-on.
4. After each session, complete the assignment in `homework/` and commit your work before the next class.
5. Using Git daily to save your work is part of the training itself — by Week 3 it will be second nature.

If you found this repository and want to learn along:

Everything here is self-contained and free to follow. Start at `week-01-linux/` and work forward in order. All you need is a computer with a terminal (WSL on Windows, Terminal on Mac, or a browser-based Linux shell).

---

## Certification path

Certifications validate the skills, while the portfolio and interview practice convert them into offers. The suggested order:

1. **GitHub Foundations** — a quick win during Month 2 that proves your CI/CD skills.
2. **AWS Certified Cloud Practitioner** — the entry ticket for cloud roles, taken around Month 3.
3. **AWS Solutions Architect Associate**, then **Certified Kubernetes Administrator (CKA)** — after the course, as you apply for roles.

---

## About

This course was designed and is taught by a practising Platform and DevOps Engineer, built around the same tools and workflows used to run real GxP-validated, cloud-native platforms on AWS in production.

The guiding principle throughout: consistency beats intensity, and you learn DevOps by doing it, not by reading about it.