# main.py
from agents.orchestrator import orchestrate_code_analysis
import json


if __name__ == "__main__":
    sample_code = """
public class BuggySQLExample {

    public static boolean loginUser(String username, String password) {
        String query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "';";
        System.out.println("Executing query: " + query);
        return executeQuery(query);
    }

    public static String getUserRole(String username) {
        // Hardcoded role retrieval for demonstration purposes
        if (username.equals("admin")) {
            return "Administrator";
        } else {
            return "User";
        }
    }

    public static String sanitizeInput(String input) {
        return input.replace("'", "''");
    }

    private static boolean executeQuery(String query) {
        // Simulate a successful query execution
        return query.contains("admin");
    }

    public static void main(String username, String password) {
        username = sanitizeInput(username);
        password = sanitizeInput(password);
        if (loginUser(username, password)) {
            System.out.println("Login successful for user: " + username);
            System.out.println("User role: " + getUserRole(username));
        } else {
            System.out.println("Login failed for user: " + username);
        }

        String sanitizedUsername = sanitizeInput(username);
        System.out.println("Sanitized username: " + sanitizedUsername);
    }
}

    """
    results = orchestrate_code_analysis(sample_code)
    

    print("Analysis Results:")
    print(json.dumps(results['functions'], indent=4))  # Pretty-print the functions
    print("\nVulnerabilities:")
    print(json.dumps({"response": results['vulnerabilities']}, indent=4)) 

