# Google Cloud Project Switcher (gswitch) 🚀

`gswitch` is a high-performance Python utility designed to streamline the workflow for engineers working across multiple Google Cloud Platform (GCP) projects. It automates the process of switching projects, authenticating accounts, syncing Application Default Credentials (ADC), and updating Kubernetes contexts.

---

## 🌟 Key Features

| Feature | Description |
| :--- | :--- |
| **Project Selection** | Interactive selection via `fzf` or direct suffix-based switching. |
| **Auth Enforcement** | Forces authentication for a specific user (default: `gswitch@gmail.com`). |
| **ADC Synchronization** | Automatically syncs Application Default Credentials and sets the quota project. |
| **GKE Integration** | Lists and configures `kubectl` context for GKE clusters in the selected project. |
| **Browser Selection** | Use `GSWITCH_BROWSER` to specify an authentication browser or use the system default. |
| **Headless Support** | Support for `--no-launch-browser` for remote server environments. |
| **Prompt Awareness** | Triggers `oh-my-posh` notifications to ensure terminal prompts reflect changes. |

---

## 🛠 Prerequisites

Ensure you have the following installed and configured:

- **Python 3.6+**
- **Google Cloud SDK (`gcloud`)**
- **fzf** (Optional, but highly recommended for interactive selection)
- **kubectl** (Optional, for GKE context switching)
- **Google Chrome** (Optional, or any browser of choice)

---

## 🚀 Usage

### Interactive Selection
Run the command without arguments to fetch a list of active projects:
```bash
gswitch
```

### Direct Switch (Shortcut)
Provide a suffix to immediately switch to a project using the prefix defined in `GSWITCH_PREFIX` (defaults to none):
```bash
# If GSWITCH_PREFIX="gcpprefix-"
gswitch dev  # Switches to gcpprefix-dev

# If GSWITCH_PREFIX is not set
gswitch my-project  # Switches to my-project
```

### Remote/Headless Mode
Use the `--no-launch-browser` flag when working over SSH or in environments without a GUI:
```bash
gswitch --no-launch-browser
```

---

## 🔍 Deep Dive

### 1. Dedicated `gcloud` Configuration
`gswitch` uses a dedicated `gcloud` configuration named `gswitch`. This prevents your primary/default `gcloud` configuration from being mutated unexpectedly.

### 2. Browser Authentication Flow
To ensure a consistent login experience, `gswitch` can override the `BROWSER` environment variable if `GSWITCH_BROWSER` is set. This is particularly useful on macOS if you want to force Google Chrome to bypass system defaults that might interfere with SSO or corporate authentication plugins.

### 3. Application Default Credentials (ADC)
One of the most common pain points in GCP development is mismatching ADC and `gcloud` project/account state. `gswitch`:
- Checks if the current ADC account matches the target email.
- Triggers `gcloud auth application-default login` if needed.
- Sets the `quota-project` to the target project, ensuring that API calls (like Vertex AI or Cloud Storage) are billed correctly and don't hit "project not found" errors.

### 4. Kubernetes (GKE) Context Switching
If `kubectl` is installed, `gswitch` will:
- List all GKE clusters in the newly selected project.
- Provide an interactive `fzf` menu to select a cluster.
- Automatically run `gcloud container clusters get-credentials` to update your `kubeconfig`.

## ⚙️ Configuration

You can override the default user email and project prefix by setting environment variables:

```bash
export GSWITCH_USER_EMAIL="gswitch@gmail.com"
export GSWITCH_PREFIX="gcpprefix-"
export GSWITCH_BROWSER="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```

---

> [!TIP]
> Add `alias gs='gswitch'` to your `.zshrc` or `.bash_profile` for even faster project switching!

> [!IMPORTANT]
> By default, `gswitch` uses your system's default browser. Set `GSWITCH_BROWSER` if you need to enforce a specific browser path (e.g., Google Chrome on macOS).

---

## 📜 Metadata
- **Language**: Python 3
- **Location**: `~/.config/bin/gswitch`
