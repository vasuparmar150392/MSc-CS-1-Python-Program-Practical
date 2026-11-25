import shutil
import subprocess
import sys

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 45: Use dig Command to Find IP Address and Display DNS Records")
print("-" * 50)


def get_domain():
    if len(sys.argv) > 1:
        return sys.argv[1].strip()

    try:
        return input("Enter domain name: ").strip()
    except EOFError:
        return "google.com"


def run_dns_query(domain, record):
    dig_path = shutil.which("dig")
    nslookup_path = shutil.which("nslookup")

    if dig_path:
        result = subprocess.run(
            [dig_path, "+short", domain, record],
            capture_output=True,
            text=True,
            check=False,
        )
        output = result.stdout.strip()
        if output:
            return output
        return result.stderr.strip() or f"No {record} record found."

    if nslookup_path:
        if record == "A":
            command = [nslookup_path, domain]
        else:
            command = [nslookup_path, "-type=" + record, domain]

        result = subprocess.run(command, capture_output=True, text=True, check=False)
        output = result.stdout.strip()
        if output:
            return output
        return result.stderr.strip() or f"No {record} record found."

    return "DNS tool not available. Install dig or use a Windows system with nslookup."


domain = get_domain()
if not domain:
    domain = "google.com"

print(f"\nDomain: {domain}")
print("\nIP Address:")
print(run_dns_query(domain, "A"))

print("\nDNS Records:")
for record in ["A", "MX", "NS", "TXT"]:
    print(f"\n{record} Records:")
    print(run_dns_query(domain, record))