# Restful endpoints for Cheeper

| Method   | Slug                                    | Description                                                                   | Who's allowed                    | Tested |
|----------|-----------------------------------------|-------------------------------------------------------------------------------|----------------------------------|--------|
| `POST`   | `/auth/login/`                          | Creates and returns an auth. token                                            | With valid login credentials     |        |
| `DELETE` | `/auth-token/`                          | Invalidates request's auth. token (will be rethought)                         | With valid token                 |        |
| `GET`    | `/users/`                               | Retrieves the list of all users (will be replaced by search)                  | Anyone                           |   OK   |
| `POST`   | `/users/`                               | Creates a new user, as part of creating a new account                         | Anyone                           |        |
| `GET`    | `/users/:user-id/`                      | Retrieves details of a specific user                                          | Anyone                           |   OK   |
| `DELETE` | `/users/:user-id/`                      | Deletes a specific user, as part of closing an account                        | Logged in as :user-id            |        |
| `GET`    | `/cheeps/`                              | Retrieves the list of all cheeps (will be replaced by search)                 | Anyone                           |        |
| `POST`   | `/cheeps/`                              | Creates a new cheep                                                           | Logged in users                  |        |
| `GET`    | `/cheeps/:cheep-id/`                    | Retrieves details of a specific cheep                                         | Anyone                           |        |
| `PATCH`  | `/cheeps/:cheep-id/`                    | Updates details of a specific cheep                                           | Logged in as author of :cheep-id |        |
| `DELETE` | `/cheeps/:cheep-id/`                    | Deletes a specific cheep                                                      | Logged in as author of :cheep-id |        |
| `GET`    | `/users/:user-id/cheeps/`               | Retrieve the list of `:user-id`'s cheeps                                      | Anyone                           |        |
| `GET`    | `/users/:user-id/following/`            | Retrieves the list of users that `:user-id` is following                      | Logged in users                  |        |
| `POST`   | `/users/:user-id/following/`            | Adds user to the list that `:user-id` is following                            | Logged in as :user-id            |        |
| `DELETE` | `/users/:user-id/following/:user-id-2/` | Removes `:user-id-2` from the list that `:user-id` is following               | Logged in as :user-id            |        |
| `GET`    | `/users/:user-id/followers/`            | Retrieves the list of users that follow `:user-id`                            | Logged in users                  |        |
| `GET`    | `/my_timeline/`                         | Retrieves the list of all cheeps from :user-id and the users that they follow | Logged in as :user-id            |        |
| `PATCH`  | `/my_profile/`                          | Updates details of the specific user one is logged in as (`:user-id`)         | Logged in as :user-id            |        |
