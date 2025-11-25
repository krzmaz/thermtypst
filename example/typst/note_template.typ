// Date formatting
#let due_date(note_data) = {
  text(
    underline(
      stroke: 2pt,
      offset: 3pt,
      box[#h(1fr)️⚠️
        #if note_data.time.len() > 0 [
          #note_data.time
        ]
        #note_data.date
      ],
    ),
  )
}

#let note(note_data) = {
  let rotation = if note_data.flip {
    180deg
  } else {
    0deg
  }
  page(width: 80mm, height: auto, margin: (x: 4mm, top: 4mm, bottom: 6mm), rotate(rotation, [
    #set text(20pt, hyphenate: true)
    #set par(leading: 0.4em)
    #align(center, [
      #note_data.text
      #if note_data.date.len() > 0 [
        #due_date(note_data)
      ]
    ])
  ]))
}

