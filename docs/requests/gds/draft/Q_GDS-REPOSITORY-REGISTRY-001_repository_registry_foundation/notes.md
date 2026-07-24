# Notes

- No incompatible Repository Identity Registry existed at Startup.
- Existing Execution Authority and Capability registries remain separate.
- GameGhost was inspected read-only using command-scoped `safe.directory`; no
  global Git configuration or GameGhost file was changed.
- GameGhost local root is nested while its remote identifies GrayGhostArchive;
  the Registry records both facts without treating the remote name as local ID.
- Planned AI artifact exchange and AllArchive entries keep root/remote UNKNOWN.
- No repository was created or initialized.
