# Restful endpoints for Cheeper

| Method   | Slug                                    | Description                                                                   | Who's allowed                    | Tested |
|----------|-----------------------------------------|-------------------------------------------------------------------------------|----------------------------------|--------|
| `POST`   | `/auth/login/`                          | Creates and returns an auth. token                                            | With valid login credentials     |        |
| `DELETE` | `/auth-token/`                          | Invalidates request's auth. token (will be rethought)                         | With valid token                 |        |
| `GET`    | `/users/`                               | Retrieves the list of all users (will be replaced by search)                  | Anyone                           |   OK   |
| `POST`   | `/users/`                               | Creates a new user, as part of creating a new account                         | Anyone                           |   OK   |
| `GET`    | `/users/:user-id/`                      | Retrieves details of a specific user                                          | Anyone                           |   OK   |
| `PATCH`  | `/users/:user-id/`                      | Updates details of a specific user (might be replaced by `/my_profile/`       | Logged in as :user-id            |   OK   |
| `DELETE` | `/users/:user-id/`                      | Deletes a specific user, as part of closing an account                        | Logged in as :user-id            |   OK   |
| `GET`    | `/cheeps/`                              | Retrieves the list of all cheeps (will be replaced by search)                 | Anyone                           |   OK   |
| `POST`   | `/cheeps/`                              | Creates a new cheep                                                           | Logged in users                  |   OK   |
| `GET`    | `/cheeps/:cheep-id/`                    | Retrieves details of a specific cheep                                         | Anyone                           |   OK   |
| `PATCH`  | `/cheeps/:cheep-id/`                    | Updates details of a specific cheep                                           | Logged in as author of :cheep-id |   OK   |
| `DELETE` | `/cheeps/:cheep-id/`                    | Deletes a specific cheep                                                      | Logged in as author of :cheep-id |   OK   |
| `GET`    | `/users/:user-id/cheeps/`               | Retrieve the list of `:user-id`'s cheeps                                      | Anyone                           |        |
| `GET`    | `/users/:user-id/following/`            | Retrieves the list of users that `:user-id` is following                      | Logged in users                  |        |
| `POST`   | `/users/:user-id/following/`            | Adds user to the list that `:user-id` is following                            | Logged in as :user-id            |        |
| `DELETE` | `/users/:user-id/following/:user-id-2/` | Removes `:user-id-2` from the list that `:user-id` is following               | Logged in as :user-id            |        |
| `GET`    | `/users/:user-id/followers/`            | Retrieves the list of users that follow `:user-id`                            | Logged in users                  |        |
| `GET`    | `/my_timeline/`                         | Retrieves the list of all cheeps from :user-id and the users that they follow | Logged in as :user-id            |        |
