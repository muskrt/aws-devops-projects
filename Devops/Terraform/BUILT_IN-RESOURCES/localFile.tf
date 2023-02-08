resource "local_file" "dbendpoint" {
  content  = "test"
  filename = "./dbserver.dbendpoint"
}
