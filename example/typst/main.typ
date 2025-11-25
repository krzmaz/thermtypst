#import "note_template.typ": note

#let note_data = json(bytes(sys.inputs.note_data))

// can be used for testing

// #let note_data = (
//   text: "testing 123",
//   date: "2025-11-25",
//   time: "11:15",
//   flip: false,
// )

#note(note_data)
